import os
import yaml
import glob


_PACKAGE_ROOT = os.path.abspath(os.path.dirname(__file__))


def _locate_directory(name):
    path = os.path.join(_PACKAGE_ROOT, name)
    if os.path.exists(path):
        return path

    path = os.path.join(_PACKAGE_ROOT, "..", name)
    if os.path.exists(path):
        return path

    raise RuntimeError(f"Unable to locate {name} directory")


SCHEMAS_ROOT = _locate_directory("schemas")
STANDARDS_ROOT = _locate_directory("standards")


def _get_paths_by_id(root):
    result = {}
    for path in glob.glob(os.path.join(root, "**", "*.yaml"), recursive=True):
        with open(path) as f:
            id = yaml.safe_load(f.read())["id"]
            result[id] = path
    return result


STANDARD_PATHS_BY_ID = _get_paths_by_id(STANDARDS_ROOT)