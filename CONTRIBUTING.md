# Contributing to Awesome Scoop

First off, thank you for considering contributing to Awesome Scoop! It's people like you that make this ecosystem great.

This document serves as a guide for developers who want to contribute to the repository. We have invested heavily in a world-class Developer Experience (DX) to ensure your time is spent writing code, not fighting tools.

## Architecture Overview

Awesome Scoop is powered by an automated GitHub crawler that discovers, ranks, and updates a curated list of Scoop and Shovel buckets.

The application is packaged as a modern Python tool managed by `uv`. The source code lives in the `maintenance/` directory and is split into distinct modules:
- `api.py`: GitHub API interactions, rate limiting, and schema fetching.
- `cache.py`: Local state persistence to avoid redundant API calls.
- `repo.py`: Git cloning, manifest traversal, and schema validation.
- `metrics.py`: The ranking algorithm (`get_repo_score`) that powers the "Trending" and "Hidden Gems" categories.
- `output.py`: Jinja2 templating for `README.md` and JSON API generation.
- `github_crawler.py`: The main orchestrator.

## Local Development Setup

We use [uv](https://github.com/astral-sh/uv) to manage our Python environment, dependencies, and tooling. It is incredibly fast and ensures reproducible builds.

### 1. Install `uv`
If you don't have `uv` installed, install it via:
```bash
# macOS / Linux
curl -LsSf https://astral.sh/uv/install.sh | sh

# Windows
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

### 2. Clone and Sync
Clone the repository and sync the dependencies. `uv` will automatically create a virtual environment (`.venv`) in the project root and install everything you need.
```bash
git clone https://github.com/mcunha/scoop-radar.git
cd scoop-radar
uv sync --all-extras --dev
```

### 3. Set up GitHub Authentication (Required)
To prevent hitting GitHub's anonymous rate limits (60 requests/hour) while testing the crawler, you must provide a GitHub Personal Access Token.
1. Create a Personal Access Token (Classic) with **no specific scopes required** (read-only public access is fine).
2. Create a `.env` file in the root of the project:
   ```bash
   echo "GITHUB_TOKEN=ghp_your_token_here" > .env
   ```
The crawler uses `python-dotenv` and will automatically load this file.

### 4. Install Pre-commit Hooks
We use `pre-commit` to ensure code quality before you even push. Install the hooks locally:
```bash
uv run pre-commit install
```

## Running the Crawler

Once your environment is set up, you can run the crawler locally using the packaged executable entry point:

```bash
uv run scoop-radar-updater
```

This will:
1. Fetch schemas.
2. Search GitHub for new buckets.
3. Update local git clones in the `maintenance/cache/` directory.
4. Calculate scores.
5. Generate a fresh `README.md` and update the JSON APIs.

## Testing

We maintain a rigorous >90% code coverage standard using a comprehensive suite of unit tests, property-based fuzzing, and micro-benchmarks.

To run the entire test suite:
```bash
uv run pytest
```

Our testing stack includes:
- **`pytest`**: The core test runner.
- **`pytest-cov`**: Generates terminal coverage reports to ensure branches aren't missed.
- **`pytest-mock` & `responses`**: Isolates tests from the filesystem and network, ensuring they run blazingly fast without mutating your local cache or hitting GitHub API rate limits.
- **`hypothesis`**: Performs property-based fuzzing on our ranking algorithms to catch edge cases (like extreme staleness or massive bucket sizes).
- **`pytest-benchmark`**: Tracks the execution speed of our core algorithms to prevent performance regressions.

## Formatting & Linting

**You do not need to worry about formatting discussions on PRs.**

We use [Ruff](https://docs.astral.sh/ruff/) to enforce a strict subset of PEP8 and the Google Python Style Guide for docstrings.

If you violate a formatting rule, one of two things will happen:
1. Your local `pre-commit` hook will intercept your commit, automatically fix the file, and ask you to stage the fixes.
2. If you bypass the local hooks, our **GitHub Actions Auto-Format Bot** will automatically fix your Pull Request and push a new commit directly to your branch.

If you want to manually trigger the formatter locally, run:
```bash
uv run ruff format .
uv run ruff check . --fix
```

## Pull Request Process

1. Create a feature branch (`git checkout -b feature/my-new-feature`).
2. Write your code and ensure you add tests for any new logic.
3. Run the test suite (`uv run pytest`) to ensure you haven't dropped the overall code coverage.
4. Commit your changes (pre-commit hooks will automatically format your code).
5. Push to your branch and open a Pull Request.

Our CI pipeline will automatically run the tests and linter against your PR. Once everything is green, a maintainer will review your logic.

---
*Happy coding!*
