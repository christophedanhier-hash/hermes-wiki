#!/usr/bin/env python3
"""Clean up temp helper scripts."""
import subprocess, os

repo = "/home/tofdan/Projets_Dev/hermes-wiki"
for fn in ["normalize_footers.py", "commit_footers.sh"]:
    fp = os.path.join(repo, fn)
    if os.path.exists(fp):
        os.remove(fp)
        print(f"Removed {fn}")

# Verify clean status
subprocess.run(["git", "status", "--short"], cwd=repo)
