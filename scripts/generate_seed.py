import concurrent.futures
import hashlib
import json
import os
import subprocess


def hash_recipe(repo_full_name, recipe_name):
    """Generate a short hash for a repository and recipe combination."""
    key = f"{repo_full_name}:{recipe_name}"
    return hashlib.md5(key.encode()).hexdigest()[:12]


def get_file_creation_date(repo_path, file_path):
    """Get the creation Unix timestamp of a file using git."""
    try:
        # git log --diff-filter=A --format="%at" -1 -- <file>
        # This gets the author date of the commit that added the file
        result = subprocess.run(
            ["git", "log", "--diff-filter=A", "--format=%at", "-1", "--", file_path],
            cwd=repo_path,
            capture_output=True,
            text=True,
            check=True,
        )
        out = result.stdout.strip()
        if out:
            # If multiple commits are returned (e.g., added, deleted, re-added), take the oldest
            dates = [int(line) for line in out.splitlines() if line.strip().isdigit()]
            if dates:
                return min(dates)
    except subprocess.CalledProcessError:
        pass
    return None


def process_repository(repo):
    """Clone a repository, find all recipes, and determine their creation dates."""
    full_name = repo["full_name"]
    git_url = repo["git_url"]

    # We need a deep clone for this, but we can put it in a temp dir
    repo_dir = f"temp_seed_clones/{full_name.replace('/', '+')}"

    print(f"[*] Seeding {full_name}...")

    if not os.path.exists(repo_dir):
        try:
            # We need full history to find creation dates, so no depth limit
            subprocess.run(["git", "clone", "--quiet", git_url, repo_dir], check=True)
        except subprocess.CalledProcessError:
            print(f"[!] Failed to clone {full_name}")
            return {}

    ages = {}

    # Find manifests
    for root_dir in [repo_dir, os.path.join(repo_dir, "bucket")]:
        if os.path.isdir(root_dir):
            for file_name in os.listdir(root_dir):
                if (
                    file_name.endswith(".json")
                    or file_name.endswith(".yaml")
                    or file_name.endswith(".yml")
                ):
                    file_path = os.path.join(root_dir, file_name)
                    if os.path.isfile(file_path):
                        # Get relative path for git command
                        rel_path = os.path.relpath(file_path, repo_dir)
                        # We must use forward slashes for git
                        rel_path = rel_path.replace("\\", "/")

                        creation_date = get_file_creation_date(repo_dir, rel_path)

                        if creation_date is not None:
                            recipe_hash = hash_recipe(full_name, file_name)
                            ages[recipe_hash] = creation_date

    # Clean up the clone to save disk space
    import shutil

    try:
        # On Windows, we might need to handle read-only files created by git
        def remove_readonly(func, path, _):
            import stat

            os.chmod(path, stat.S_IWRITE)
            func(path)

        shutil.rmtree(repo_dir, onerror=remove_readonly)
    except Exception as e:
        print(f"[!] Failed to clean up {repo_dir}: {e}")

    return ages


def main():
    if not os.path.exists("all.json"):
        print("[!] all.json not found. Run the crawler first to generate the ecosystem data.")
        return

    with open("all.json", encoding="utf-8") as f:
        data = json.load(f)

    repos = data.get("all", [])
    if not repos:
        print("[!] No repositories found in all.json.")
        return

    os.makedirs("temp_seed_clones", exist_ok=True)

    seed_data = {"last_seed_generation": 0, "ages": {}}

    # If we already have a seed file, load it so we don't start from scratch
    if os.path.exists("recipe_ages.json"):
        with open("recipe_ages.json", encoding="utf-8") as f:
            try:
                seed_data = json.load(f)
                print(f"[*] Loaded existing seed data with {len(seed_data['ages'])} entries.")
            except json.JSONDecodeError:
                pass

    # We only process a few repos at a time to save disk space
    with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
        future_to_repo = {executor.submit(process_repository, repo): repo for repo in repos}

        for future in concurrent.futures.as_completed(future_to_repo):
            repo = future_to_repo[future]
            try:
                repo_ages = future.result()
                if repo_ages:
                    seed_data["ages"].update(repo_ages)
            except Exception as e:
                print(f"[!] Exception processing {repo['full_name']}: {e}")

    import time

    seed_data["last_seed_generation"] = int(time.time())

    with open("recipe_ages.json", "w", encoding="utf-8") as f:
        json.dump(seed_data, f, separators=(",", ":"))

    print(f"[*] Seed generation complete. Indexed {len(seed_data['ages'])} recipes.")

    try:
        os.rmdir("temp_seed_clones")
    except OSError:
        pass


if __name__ == "__main__":
    main()
