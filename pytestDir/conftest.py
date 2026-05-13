# global file for fixture: conftest.py
# run all files : python -m pytest  OR pytest -s (-s to print values)
# run a single file : pytest test_fileName.py
# run a single test : pytest test_fileName.py::test_functionName
# skipp test : @pytest.mark.skip -> annotation to skip the function/ test
# tagging (run set of tests) : @pytest.mark.tagName
# run tests using tags: pytest -m smoke
import pytest


@pytest.fixture(scope="session")
def preSetupWork():
    print("I setup session instance")