import os
import pytest
# from session11 import *

def test_readme_exists():
    assert os.path.isfile("README.md"), "README.md file missing!"
