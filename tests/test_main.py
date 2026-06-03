"""
Example test of the main script.
Note: Test the project only if applicable/necessary. You
can create as many tests as you wish.

"""

from src.main import main

def test_main():
    result = main()
    assert result == 'abc'

test_main()