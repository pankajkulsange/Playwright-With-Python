# playwright => global fixer
# chromium engine => Google Chrome and, MS Edge
# run by using command : pytest test_playwrightBasics.py::test_playwrightShortcut --headed
from playwright.sync_api import Page

def test_playwrightBasics(playwright):
    browser = playwright.chromium.launch(headless=False)
    # open an incognito page
    context = browser.new_context() # cookies and caches stored e.g. login cookies
    # open new page
    page = context.new_page()
    page.goto("https://rahulshettyacademy.com/")

# chromium headless mode, 1 single context
def test_playwrightShortcut(page: Page):
    page.goto("https://rahulshettyacademy.com/")

# learning locators
def test_loginWithValidCredentials(page: Page):
    page.goto("https://rahulshettyacademy.com/loginpagePractise/")
    # get by label
    page.get_by_label("Username:").fill("rahulshettyacademy")
    page.get_by_label("Password:").fill("Learning@830$3mK2")
    page.get_by_role("combobox").select_option("teach")
    page.locator("#terms").click()
    page.get_by_role("button", name="Sign In").click()

