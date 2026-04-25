import io
import os
import zipfile

import requests
from dotenv import load_dotenv


def main():
    load_dotenv()

    token = os.environ.get("GITHUB_TOKEN")
    if not token:
        print("[!] GITHUB_TOKEN environment variable is not set in .env")
        print("    Please add it to download the cache artifact.")
        return

    headers = {
        "Authorization": f"Bearer {token}",
        "Accept": "application/vnd.github.v3+json",
        "User-Agent": "Scoop-Radar-Sync",
    }

    repo = "mcunha/scoop-radar"

    print(f"[*] Fetching recent artifacts for {repo}...")
    artifacts_url = (
        f"https://api.github.com/repos/{repo}/actions/artifacts?name=crawler-cache&per_page=1"
    )

    response = requests.get(artifacts_url, headers=headers)
    if response.status_code != 200:
        print(f"[!] Failed to fetch artifacts: {response.status_code}")
        print(response.text)
        return

    data = response.json()
    artifacts = data.get("artifacts", [])

    if not artifacts:
        print(
            "[!] No 'crawler-cache' artifact found. The GitHub Action may not have finished running yet."
        )
        return

    artifact = artifacts[0]
    download_url = artifact["archive_download_url"]

    print(f"[*] Found artifact from {artifact['created_at']}. Downloading...")

    dl_response = requests.get(download_url, headers=headers)
    if dl_response.status_code != 200:
        print(f"[!] Failed to download artifact: {dl_response.status_code}")
        return

    print("[*] Extracting cache.pickle...")

    os.makedirs("maintenance", exist_ok=True)

    try:
        with zipfile.ZipFile(io.BytesIO(dl_response.content)) as z:
            if "cache.pickle" in z.namelist():
                # Extract to memory then write to right place just in case the zip paths are weird
                cache_data = z.read("cache.pickle")
                with open(os.path.join("maintenance", "cache.pickle"), "wb") as f:
                    f.write(cache_data)
                print("[*] Successfully synced maintenance/cache.pickle!")
            else:
                print("[!] cache.pickle not found in the downloaded artifact.")
    except Exception as e:
        print(f"[!] Failed to extract artifact: {e}")


if __name__ == "__main__":
    main()
