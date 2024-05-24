from typing import List


console_scripts: List[str] = [
    "pybookmarks=pybookmarks.main:main",
]
dev_requires: List[str] = [
    "pypitools",
    "black",
]
config_requires: List[str] = [
    "pyclassifiers",
]
install_requires: List[str] = []
build_requires: List[str] = [
    "pymakehelper",
    "pydmt",
]
test_requires: List[str] = [
    "pytest",
    "pytest-cov",
    "flake8",
    "pylint",
    "mypy",
    "types-requests",
]
requires = config_requires + install_requires + build_requires + test_requires
