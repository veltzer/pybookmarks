"""
main
"""
import sys
import json
import pylogconf.core
from pytconf import register_endpoint, register_main, config_arg_parse_and_launch

from pybookmarks.static import DESCRIPTION, APP_NAME, VERSION_STR
from pybookmarks.utils import get_accounts


@register_endpoint(
    configs=[],
    description="Show google accounts",
)
def show_accounts() -> None:
    json.dump(get_accounts(), sys.stdout, indent=4)


@register_main(
    main_description=DESCRIPTION,
    app_name=APP_NAME,
    version=VERSION_STR,
)
def main():
    pylogconf.core.setup()
    config_arg_parse_and_launch()


if __name__ == "__main__":
    main()
