from playwright.sync_api import Page, expect


def test_check_your_rate(page: Page):
    page.goto("https://evafi.relintex.dev/")

    check_rate_button = page.get_by_role("button", name="Check my rate")

    expect(check_rate_button).to_be_visible()
    check_rate_button.click()