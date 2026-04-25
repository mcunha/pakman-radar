"""Functions related to cache management."""

import os
import pickle


def load_cache(dir_path):
    """Load the cache from disk."""
    cache = {}
    try:
        with open(os.path.join(dir_path, "cache.pickle"), "rb") as input_file:
            cache = pickle.load(input_file)
    except (OSError, EOFError):
        pass

    CURRENT_CACHE_VERSION = 3
    cache_version = cache.get("CACHE_VERSION", 1)

    if cache_version < CURRENT_CACHE_VERSION:
        print(f"[*] Upgrading cache from v{cache_version} to v{CURRENT_CACHE_VERSION}...")
        if cache_version < 3:
            # Upgrade v1 -> v2: Add bucket/ prefix to entries where applicable
            repo_keys = [k for k in cache.keys() if "+" in k]
            for k in repo_keys:
                entry = cache[k]
                repo_path = os.path.join(dir_path, "cache", k)
                if "entries" in entry and os.path.isdir(repo_path):
                    new_entries = []
                    for d in [repo_path, os.path.join(repo_path, "bucket")]:
                        if os.path.isdir(d):
                            for f in os.listdir(d):
                                if (
                                    f.endswith(".json") or f.endswith(".yaml") or f.endswith(".yml")
                                ) and os.path.isfile(os.path.join(d, f)):
                                    # If the file was in the original entries list (ignoring path)
                                    if any(f == e.split("/")[-1] for e in entry["entries"]):
                                        rel_path = f"bucket/{f}" if d.endswith("bucket") else f
                                        if rel_path not in new_entries:
                                            new_entries.append(rel_path)
                    entry["entries"] = new_entries

        cache["CACHE_VERSION"] = CURRENT_CACHE_VERSION

    return cache


def save_cache(cache, dir_path):
    """Save the cache to disk."""
    try:
        with open(os.path.join(dir_path, "cache.pickle"), "wb") as input_file:
            pickle.dump(cache, input_file)
    except OSError:
        pass


def upgrade_cache_entry(repofoldername, entry):
    """Ensure a cache entry has all required default fields."""
    if "full_name" not in entry:
        entry["full_name"] = repofoldername.replace("+", "/")
    if "git_url" not in entry or entry["git_url"].startswith("git://"):
        entry["git_url"] = f"https://github.com/{entry['full_name']}.git"
    if "html_url" not in entry:
        entry["html_url"] = entry.get("url", f"https://github.com/{entry['full_name']}")
    if "default_branch" not in entry:
        entry["default_branch"] = "master"
    if "topics" not in entry:
        entry["topics"] = []
    if "last_checked" not in entry:
        entry["last_checked"] = "2000-01-01T00:00:00Z"
    if "pushed_at" not in entry:
        entry["pushed_at"] = "2000-01-01T00:00:00Z"
    if "archived" not in entry:
        entry["archived"] = False
    if "disabled" not in entry:
        entry["disabled"] = False
    if "checkver_count" not in entry:
        entry["checkver_count"] = 0
    if "consecutive_failures" not in entry:
        entry["consecutive_failures"] = 0
    return entry
