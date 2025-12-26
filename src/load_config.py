import sys
import json
from pathlib import Path

# Locate config file
CONFIG_PATH = Path(__file__).resolve().parents[1] / "config" / "paths.local.json"

# print(CONFIG_PATH)

if not CONFIG_PATH.exists():
    raise FileNotFoundError(
        "Missing config/paths.local.json. "
        "Create it from paths.example.json."
    )

# Load config
with open(CONFIG_PATH, "r") as f:
    config = json.load(f)

project_root = config.get("project_root")

if project_root and project_root not in sys.path:
    sys.path.append(project_root)