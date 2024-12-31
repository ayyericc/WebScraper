from time import sleep
from playwright.async_api import async_playwright
from playwright.sync_api import sync_playwright
from bs4 import BeautifulSoup
import asyncio



# Always set this policy at the top of your script when using Playwright or other subprocess-based asyncio libraries on Windows:
import asyncio
import platform
if platform.system() == "Windows":
    asyncio.set_event_loop_policy(asyncio.WindowsProactorEventLoopPolicy())
#-----------------------------------------------------------------------------------------------------------------------------------------------

AUTH = 'brd-customer-hl_8ef9479c-zone-selenium_tut:5wieij04vv4y'
SBR_WS_CDP = f'https://{AUTH}@brd.superproxy.io:9222'


# async def scrape_site(website):
#     async with async_playwright() as p:
#         browser = await p.chromium.connect_over_cdp(SBR_WS_CDP)
#         page = await browser.new_page()
#
#         # Navigate to the website asynchronously
#         await page.goto(website)
#         await page.wait_for_load_state("load")
#
#         # Get the HTML content asynchronously
#         html = await page.content()
#         print(html)
#         return html



def scrape_site(website, item):
    with sync_playwright() as p:
        browser = p.chromium.connect_over_cdp(SBR_WS_CDP)
        page = browser.new_page()
        page.goto(website, wait_until="domcontentloaded")
        # page.goto(f"https://{website}.com")
        # page.wait_for_load_state("load")
        # page.fill(selector= "input[aria-label= Search]", value= item)
        # page.click("button[type= submit]")
        try:
            page.click("button#accept-cookies")  # Example selector for a consent button
        except:
            print("No consent pop-up found.")

        html = page.content()
        print("page done parsing")
        return html



def extract_html_content(html_content):
    soup = BeautifulSoup(html_content, "html.parser")
    body = soup.body
    if body:
        return str(body)
    else:
        return ""


def clean_html_content(body_content):
    soup = BeautifulSoup(body_content, "html.parser")

    for script_or_style in soup(["script", "style"]):
        script_or_style()

    cleaned_content = soup.get_text(separator= "\n")
    cleaned_content = "\n".join(
        line.strip() for line in cleaned_content.splitlines() if line.strip()
    )

    return cleaned_content



def split_dom_content(dom_content, max_length= 6000):
    return [
        dom_content[i : i + max_length] for i in range(0, len(dom_content), max_length)

    ]






















# AUTH = 'brd-customer-hl_8ef9479c-zone-selenium_tut:5wieij04vv4y'
# SBR_WS_CDP = f'https://{AUTH}@brd.superproxy.io:9222'
#
# with sync_playwright() as p:
#     browser = p.chromium.connect_over_cdp(SBR_WS_CDP)
#     page = browser.new_page()
#     page.goto("https://www.amazon.com")
#     page.wait_for_selector("div#nav-logo")
#     page.screenshot(path="example.png")
#     browser.close()
#     print("image captured")
#




#
# def target_search(user_item):
#     with sync_playwright() as p:
#         browser = p.chromium.launch(headless= False) #creates the playwright object
#         page = browser.new_page() # creates a new page
#         page.goto("https://www.target.com/")
#         page.fill(selector= "input.sc-4596e520-2.dKPRDc", value= user_item)
#         page.click("button.sc-4596e520-3.eaRqyD")
#
#         # Waits for the page to load so the program can grab the link
#         page.wait_for_selector("img")  # Wait for images to appear, indicating the results have loaded
#         element = page.query_selector(f"img[alt*= '{user_item}']")  # grab the html that holds the link to the product
#         if element:
#             # Get the image source (link to the product)
#             link = element.get_attribute("src")
#         else:
#             link = "No image found"
#
#         page.click(f"a:has-text('{user_item}')") #This click the item with partial match of the searched item
#         price = page.inner_text("span:has-text('$')") #This return the price using partial text that matched with the $ sign
#
#         #Grabs the product name of the page it landed on
#         page.wait_for_selector("h1[data-test= 'product-title']")
#         name = page.inner_text("h1[data-test= 'product-title']")
#         return f"The {name} cost: {price}. You purchase the item here: {link}" #return the price of an item
#
#
#
#
# one = target_search("chocolate chip cookies")
# print(one)




# #allows the program to run while waiting for a page to load.
# async def main():
#     async with async_playwright() as p: #Runs all the code inside the with statement and closes the browser after
#         print("awaiting connection")
#         browser = await p.chromium.connect_over_cdp(SBR_WS_CDP)
#         print("connection made")
#         try:
#             page = await browser.new_page()
#             await page.goto("https://www.amazon.com", wait_until= "networkidle")
#             await page.wait_for_selector("div#nav-logo")
#             print("on amazon page")
#             await page.screenshot(path= "example.png")
#
#         finally:
#             await browser.close()
#             print("image captured")
#
# asyncio.run(main()) #This is needed with wanting to run an async function
