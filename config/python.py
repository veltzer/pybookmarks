""" python deps for this project """

scripts: dict[str,str] = {
    "pybookmarks": "pybookmarks.main:main",
}
config_requires: list[str] = [
    "pyclassifiers",
]
build_requires: list[str] = [
    "pymakehelper",
    "pydmt",
]
test_requires: list[str] = [
    "pytest",
    "pytest-cov",
    "pylint",
    "mypy",
    "types-requests",
]
requires = config_requires + build_requires + test_requires
