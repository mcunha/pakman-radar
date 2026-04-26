# Awesome Package Managers Radar

A data-driven, automated discovery and ranking engine for Windows package manager ecosystems.

This repository tracks, ranks, and analyzes community repositories (buckets/feeds) to help users discover hidden gems, trending packages, and reliable sources.

## Supported Ecosystems

*   [**Scoop & Shovel**](./scoop_shovel/README.md): The original crawler, tracking over 1,000+ buckets and 120,000+ recipes.
*   [**Chocolatey**](./chocolatey/README.md): Tracking community package sources for Chocolatey.
*   [**WinGet**](./winget/README.md): Tracking community package sources for Windows Package Manager (Coming Soon).

## How it works

The engine runs on GitHub Actions and performs the following tasks:
1.  **Discovery**: Scans GitHub for specific topics (e.g. `scoop-bucket`, `chocolatey-packages`) to find new repositories.
2.  **Validation**: Clones repositories and validates their manifests against official schemas.
3.  **Metrics**: Analyzes repository health based on update frequency, uniqueness, active maintenance, and staleness.
4.  **Generation**: Produces detailed markdown directories, SVG charts, and JSON APIs for the community to consume.

See [CONTRIBUTING.md](CONTRIBUTING.md) if you'd like to help improve the crawler.
