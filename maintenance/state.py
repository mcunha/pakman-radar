"""Global state for the maintenance crawler."""

abort_flag = False
SCOOP_SCHEMA = None
SHOVEL_SCHEMA = None
api_retries = 0
evicted_count = 0
evicted_repos = []
