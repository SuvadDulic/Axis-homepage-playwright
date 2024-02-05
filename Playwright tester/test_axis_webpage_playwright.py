import re
import asyncio
from playwright.sync_api import Page, expect, sync_playwright
import time
import pytest

AXIS_SITE = "https://www.axis.com/"


with sync_playwright() as p:
    browser = p.chromium.launch(headless=False, args=["--start-maximized"])

    #browser = p.chromium.launch(headless=False, args=[])
    time.sleep(5)
    browser.new_context(no_viewport=True)
    browser.close()

#@pytest.mark.skip(reason="Will finish later")
def test_axis_homepage(page: Page):

    #page = browser.new_page()

    #browser = p.chromium.launch(headless=False, args=["--start-maximized"])

    #context = browser.new_context(no_viewport=True)

    #page = context.new_page()

    page.goto(AXIS_SITE)

    # Expect a title "to contain" a substring.
    expect(page).to_have_title(re.compile("Axis"))

def test_solutions_page_link(page: Page):

    page.goto(AXIS_SITE)
    
    page.context

    #Click on popup
    page.get_by_role("button", name="Only Necessary").click()

    page.get_by_role("link", name="Solutions", exact=True).click()
    # Verfiy that page link works by finding heading that contains page name solutions
    expect(page.locator("h1")).to_contain_text("Solutions")

def test_products_page_link(page: Page):

    page.goto(AXIS_SITE)


    #Click on popup
    page.get_by_role("button", name="Only Necessary").click()

    # Find product page link in home page and then click on the link
    page.get_by_role("link", name="Products", exact=True).click()

    expect(page.locator("h1")).to_contain_text("Products")

    #page.mouse.wheel(0, 1000)

    #page.get_by_role("link", name="Network cameras", exact=True).click()

    #element = page.locator("text=Network cameras").locator("..")

    #element.click()

def test_learning_page_link(page: Page):

    page.goto(AXIS_SITE)

    #Click on popup
    page.get_by_role("button", name="Only Necessary").click()

    page.get_by_role("link", name="Learning", exact=True).click()

    expect(page.get_by_role("heading", name="Learning", exact=True).locator("span"))

def test_support_page_link(page: Page):

    page.goto(AXIS_SITE)

    page.get_by_role("button", name="Only Necessary").click()

    page.get_by_role("link", name="Support", exact=True).click()

    expect(page.locator("h1")).to_contain_text(re.compile("Support", re.IGNORECASE))

def test_partner_page_link(page: Page):

    page.goto(AXIS_SITE)

    #Click on popup
    page.get_by_role("button", name="Only Necessary").click()

    page.get_by_label("Main navigation").get_by_role("link", name="Partner", exact=True).click()

    expect(page.locator("h1")).to_contain_text(re.compile("partner", re.IGNORECASE))

def test_wheretobuy_page_link(page: Page):

    page.goto(AXIS_SITE)

    #Click on popup
    page.get_by_role("button", name="Only Necessary").click()

    page.get_by_role("link", name="WHERE TO BUY").click()

    expect(page.locator("h1")).to_contain_text("Where to buy")

def test_newsroom_page_link(page: Page):

    page.goto(AXIS_SITE)

    # Click on popup
    page.get_by_role("button", name="Only Necessary").click()

    page.get_by_role("link", name="View all news").click()

    expect(page).to_have_title(re.compile("newsroom", re.IGNORECASE))

def test_contact_us_page_link(page: Page):

    page.goto(AXIS_SITE)

    # Click on popup
    page.get_by_role("button", name="Only Necessary").click()

    page.get_by_label("contact us").click()

    expect(page).to_have_title(re.compile("contact us", re.IGNORECASE))

def test_login_page_link(page: Page):

    page.goto(AXIS_SITE)

    # Click on popup
    page.get_by_role("button", name="Only Necessary").click()

    page.get_by_label("log in").click()

    expect(page).to_have_title(re.compile("Sign in", re.IGNORECASE))

def test_axis_searchbar(page: Page):

    page.goto(AXIS_SITE)

    # Click on popup
    page.get_by_role("button", name="Only Necessary").click()
    # Find the searchbar and then input camera in searchbar
    page.get_by_label("search").fill("camera")

    page.locator("button").filter(has_text="search").click()

    # Find first search result and click it
    page.locator(".gs-title").locator("nth = 1").click()
    # Verify that first search result is relevant to the search word
    expect(page).to_have_title(re.compile("camera", re.IGNORECASE))

def test_customerstory_page_link(page: Page):

    page.goto(AXIS_SITE)

    page.get_by_role("button", name="Only Necessary").click()

    page.get_by_role("link", name="View all customer stories").click()

    expect(page).to_have_title(re.compile("customer stories", re.IGNORECASE))

def test_corpgover_page_link(page: Page):

    page.goto(AXIS_SITE)

    find_popup = page.get_by_role("button", name="Only Necessary").is_visible()

    if find_popup:

        page.get_by_role("button", name="Only Necessary").click()

    page.get_by_role("link", name="Corporate governance").click()

    expect(page).to_have_title(re.compile("corporate governance", re.IGNORECASE))