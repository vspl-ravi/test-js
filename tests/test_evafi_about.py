from playwright.sync_api import sync_playwright


def test_about_and_how_eva_works():

    with sync_playwright() as p:

        # Open visible browser
        browser = p.chromium.launch(
            headless=False,
            slow_mo=500
        )

        page = browser.new_page()

        # Open EvaFi
        page.goto(
            "https://evafi.relintex.dev/",
            wait_until="domcontentloaded"
        )

        # Wait 3 seconds
        page.wait_for_timeout(3000)

        # Click About
        about_link = page.locator(
            "#site-navbar"
        ).get_by_role(
            "link",
            name="About"
        )

        about_link.wait_for(state="visible")
        about_link.click()

        # Wait for About page
        page.wait_for_load_state("domcontentloaded")
        page.wait_for_url("**/about")

        print("About page loaded successfully")

        # Find How Eva works
        how_eva_works = page.get_by_role(
            "button",
            name="How Eva works"
        )

        how_eva_works.wait_for(state="visible")

        # Click
        how_eva_works.click()

        # Wait
        page.wait_for_load_state("domcontentloaded")

        print("How Eva works clicked successfully")
        print("Current URL:", page.url)

        # Keep browser open for 5 seconds
        page.wait_for_timeout(5000)

        browser.close()