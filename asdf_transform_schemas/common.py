import os


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
