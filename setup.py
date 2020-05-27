#!/usr/bin/env python
import os

from setuptools import setup

import os


package_dir = {}
packages = ["asdf_transform_schemas"]
for directory in ["schemas"]:
    for walk_result in os.walk(directory):
        path = walk_result[0]
        package = ".".join(["asdf_transform_schemas"] + path.split(os.sep))
        package_dir[package] = path
        packages.append(package)

setup(use_scm_version=True, package_dir=package_dir, packages=packages)
