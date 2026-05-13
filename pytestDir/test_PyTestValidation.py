# use test prefix/ postfix in function name
# Fixtures: @pytest.fixture
# scope = "module" run once for same file
# scope = "function" run before every function call (by default)
# scope = "class" run once for your entire class
# scope = "session" once across the execution (across multiple files)
import pytest


@pytest.fixture(scope="module")
def preWork():
    print("I setup module instance")
    return "pass"
@pytest.fixture(scope="function")
def secondWork():
    print("I setup browser instance function scope")
    yield # pause, execute code then continue
    print("Tear down validation")
@pytest.mark.smoke
def test_initialCheck(preWork):
    print("This is first test")
    assert preWork == "pass"
    # assert preWrok == "fail"
def test_secondCheck(preSetupWork, secondWork):
    print("This is second test")