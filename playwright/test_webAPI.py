
from playwright.sync_api import Playwright, expect

from utils.apiBase import APIUtils


def test_e2e_webAPI(playwright: Playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()

    # create order -> get order ID
    api_utils = APIUtils()
    orderId = api_utils.createOrder(playwright)

    # login
    page.goto("https://rahulshettyacademy.com/client")
    page.get_by_placeholder("email@example.com").fill("lotela9945@ellbit.com")
    page.get_by_placeholder("enter your passsword").fill("#Punisher01")
    page.get_by_role("button", name="Login").click()

    #Navigate to orders page
    page.get_by_role("button", name="ORDERS").click()

    # orders history page -> order is present
    row = page.locator("tr").filter(has_text=orderId)
    row.get_by_role("button", name="View").click()

    #assertion
    expect(page.locator(".tagline")).to_contain_text("Thank you for Shopping With Us")
    context.close()