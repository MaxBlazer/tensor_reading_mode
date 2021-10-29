import pytest

from tensor_reading_mode.main import wrap


def test_wrap():
    input = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et' \
            ' dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip' \
            ' ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore' \
            ' eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia' \
            ' deserunt mollit anim id est laborum.'

    output = wrap(input)

    for line in output.split('\n'):
        assert len(line) <= 80
