filepath = "maintenance/output.py"
with open(filepath, encoding="utf-8") as f:
    content = f.read()

content = content.replace(
    "def generate_growth_charts(timeseries, dir_path):",
    "def generate_growth_charts(timeseries, out_dir):",
)
content = content.replace(
    'os.path.join(dir_path, "..", f"growth_{ecosystem}_{theme_name}.svg")',
    'os.path.join(out_dir, f"growth_{ecosystem}_{theme_name}.svg")',
)

content = content.replace(
    "def generate_readme(\n    actual_repos, scoop_repos, shovel_repos, hidden_gems, trending, metrics, dir_path\n):",
    "def generate_readme(\n    actual_repos, scoop_repos, shovel_repos, hidden_gems, trending, metrics, out_dir, dir_path\n):",
)
content = content.replace(
    'buckets_dir = os.path.join(dir_path, "..", "directory")',
    'buckets_dir = os.path.join(out_dir, "directory")',
)
content = content.replace(
    'os.path.join(dir_path, "..", "README.md")', 'os.path.join(out_dir, "README.md")'
)

content = content.replace(
    "def write_api_file(filename, data_key, data_list, metrics, dir_path):",
    "def write_api_file(filename, data_key, data_list, metrics, out_dir):",
)
content = content.replace(
    'os.path.join(dir_path, "..", filename)', "os.path.join(out_dir, filename)"
)

content = content.replace(
    "def generate_apis(\n    actual_repos, scoop_repos, shovel_repos, hidden_gems, trending, evictions, metrics, dir_path\n):",
    "def generate_apis(\n    actual_repos, scoop_repos, shovel_repos, hidden_gems, trending, evictions, metrics, out_dir\n):",
)
content = content.replace("dir_path", "out_dir")
# Wait, this replaced EVERYTHING with out_dir! Let's not do that globally.
