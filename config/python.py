""" python deps for this project """

import config.shared

build_requires: list[str] = config.shared.PBUILD
test_requires: list[str] = config.shared.PTEST
types_requires: list[str] = [
    "types-requests",
]
requires = build_requires + test_requires + types_requires

scripts: dict[str,str] = {
    "pybookmarks": "pybookmarks.main:main",
}
