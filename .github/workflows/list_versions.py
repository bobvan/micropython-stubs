import json
import os
import sys

from github import Github
from packaging.version import parse


def micropython_versions(start="v1.10"):
    g = Github()
    repo = g.get_repo("micropython/micropython")
    return sorted([tag.name for tag in repo.get_tags() if parse(tag.name) >= parse(start)], reverse=True)

if __name__ == "__main__":
    matrix = {}
    add_latest = False
    if len(sys.argv) > 1:
        add_latest = sys.argv[1].lower() in ["--latest", "-l"]
    # if environ.get("ACT"):
    #     # only run latests when running in ACT locally for testing
    #     matrix["version"] = micropython_versions(start="v1.17")[-1:]
    else:
        matrix["version"] = micropython_versions(start="v1.17")
        if add_latest: # add at the start
            matrix[:0] == ["latest"]
    print(json.dumps(matrix))
    # GITHUB_OUTPUT is set by github actions
    if os.getenv('GITHUB_OUTPUT'):
        with open(os.getenv('GITHUB_OUTPUT'), 'a') as file:   #  type: ignore
            file.write(f"versions={json.dumps(matrix)}")
