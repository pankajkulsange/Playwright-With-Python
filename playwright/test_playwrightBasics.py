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

def test_coreLocators(page: Page):
    page.goto("https://rahulshettyacademy.com/loginpagePractise/")
    # get by label
    page.get_by_label("Username:").fill("rahulshettyacademy")
    page.get_by_label("Password:").fill("learning")
    page.get_by_role("combobox").select_option("teach")
    page.pause()