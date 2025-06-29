""" python deps for this project """

scripts: dict[str,str] = {
    "pybookmarks": "pybookmarks.main:main",
}
config_requires: list[str] = [
    "pyclassifiers",
]
build_requires: list[str] = [
    "hatch",
    "pydmt",
    "pymakehelper",
    "pycmdtools",
]
test_requires: list[str] = [
    "pytest",
    "pylint",
    "mypy",
    "ruff",
    # types
    "types-requests",
]
requires = config_requires + build_requires + test_requires
