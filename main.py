import os
import json
from typing import Union   # общие

import requests   # загруженные через pip

import docstring   # локальные


INDENT = 4   # константы


def main():
    print(print_json_string([1, 2, 3]))


def print_json_string(obj: Union[list, dict]) -> str:
    """

    :param obj:
    :return:
    """
    return json.dumps(obj, indent=INDENT)


if __name__ == '__main__':
    main()
