import re
import asyncio
from playwright.sync_api import Page, expect, sync_playwright
import time
import pytest

AXIS_SITE = "https://www.axis.com/"

#@pytest.mark.skip(reason="Will finish later")
def test_axis_homepage(page: Page):

    page.goto(AXIS_SITE)

    # Expect a title "to contain" a substring.
    expect(page).to_have_title(re.compile("Axis"))

def test_solutions_page_link(page: Page):

    page.goto(AXIS_SITE)
    
    page.context

    # Click on popup
    page.get_by_role("button", name="Only Necessary").click()
    # Locator for link to Solutions page, and then click on it 
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

def test_learning_page_link(page: Page):

    page.goto(AXIS_SITE)

    #Click on popup
    page.get_by_role("button", name="Only Necessary").click()

    page.get_by_role("link", name="Learning", exact=True).click()

    page_header = page.locator("h1").first

    expect(page_header).to_contain_text("Learning")  

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

    page_header = page.get_by_role("link", name="Newsroom", exact=True)

    expect(page_header).to_have_text("Newsroom")

def test_contact_us_page_link(page: Page):

    page.goto(AXIS_SITE)

    # Click on popup
    page.get_by_role("button", name="Only Necessary").click()

    page.get_by_role("link", name="contact us", exact=True).click()

    expect(page).to_have_title(re.compile("contact us", re.IGNORECASE))

def test_country_contact_info(page: Page):

    page.goto(AXIS_SITE)

    # Click on popup
    page.get_by_role("button", name="Only Necessary").click()

    page.get_by_role("link", name="contact us", exact=True).click()

    #page.locator("#edit-field-country-region-target-id").select_option(label="Sweden")

    page.locator("[name='field_country_region_target_id']").click()

    page.locator("[name='field_country_region_target_id']").select_option(label="Sweden")

    contact_info = page.wait_for_selector(".offices__result")

    contact_info_country = page.locator("p").filter(has_text="Sweden, Lund").first

    expect(page.locator(".offices__result")).to_be_visible()
    expect(contact_info_country).to_contain_text("Sweden")

def test_login_page_link(page: Page):

    page.goto(AXIS_SITE)

    # Click on popup
    page.get_by_role("button", name="Only Necessary").click()

    page.get_by_label("log in").click()

    expect(page.locator("h1")).to_contain_text("Sign in")

def test_login_register_link(page: Page):

    page.goto(AXIS_SITE)

    page.get_by_role("button", name="Only Necessary").click()

    page.get_by_label("log in").click()

    page.locator("#reg-link").click()

    expect(page.locator("h1")).to_contain_text("Create Account")

def test_login_forgot_password_link(page: Page):

    page.goto(AXIS_SITE)

    page.get_by_role("button", name="Only Necessary").click()

    page.get_by_label("log in").click()

    page.locator("#forgot-link").click()

    expect(page.locator("h1")).to_contain_text("Reset password")

def test_axis_homepage_searchbar(page: Page):

    page.goto(AXIS_SITE)

    # Click on popup
    page.get_by_role("button", name="Only Necessary").click()
    # Find the searchbar and then input camera in searchbar
    page.get_by_label("search").fill("camera")

    page.locator("button").filter(has_text="search").click()

    # Find first search result and click it
    page.locator(".gs-title").locator("nth = 1").click()
    # Verify that first search result is relevant to the search word
    expect(page.locator("h1")).to_contain_text(re.compile("cameras", re.IGNORECASE))

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

def test_sustainabilitiy_page_link(page: Page):

    page.goto(AXIS_SITE)

    find_popup = page.get_by_role("button", name="Only Necessary").is_visible()

    if find_popup:

        page.get_by_role("button", name="Only Necessary").click()

    page.get_by_role("link", name="Sustainability").click()

    expect(page.locator("h1")).to_contain_text("Sustainability")

def test_experience_center_page_link(page: Page):

    page.goto(AXIS_SITE)

    find_popup = page.get_by_role("button", name="Only Necessary").is_visible()

    if find_popup:

        page.get_by_role("button", name="Only Necessary").click()

    page.get_by_role("link", name="Experience Center").click()

    expect(page.locator("h1")).to_contain_text(re.compile("Experience center", re.IGNORECASE))

def test_cookies_settings_popup(page: Page):

    page.goto(AXIS_SITE)
    
    find_popup = page.get_by_role("button", name="Only Necessary").is_visible()

    if find_popup:

        page.get_by_role("button", name="Only Necessary").click()

        expect(page.get_by_role("button", name="Only Necessary")).not_to_be_visible()

    page.get_by_role("link", name="Cookie settings").click()

    expect(page.get_by_role("button", name="Only Necessary")).to_be_visible()

def test_change_language_swedish(page: Page):

    page.goto(AXIS_SITE)

    find_popup = page.get_by_role("button", name="Only Necessary").is_visible()

    if find_popup:

        page.get_by_role("button", name="Only Necessary").click()

    english_header = page.get_by_role("heading", name="Discover smart solutions")

    expect(english_header).to_contain_text("Discover")

    page.get_by_role("link", name="Global / English").click()

    page.get_by_role("link", name="Europe").click()

    page.get_by_role("link", name="Svenska").click()

    swedish_header = page.get_by_role("heading", name="Upptäck smarta lösningar")

    expect(swedish_header).to_contain_text("Upptäck")
