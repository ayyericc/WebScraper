from time import sleep
from playwright.sync_api import sync_playwright
from bs4 import BeautifulSoup

#
# with sync_playwright() as p: #Runs all the code inside the with statement and closes the browser after
#     browser = p.chromium.launch(headless= False, slow_mo= 50)
#     page = browser.new_page()
#     page.goto("https://www.target.com/")
#     page.fill(selector= "input.sc-4596e520-2.dKPRDc", value= "ps5")
#     page.click("button.sc-4596e520-3.eaRqyD")



def target_search(user_item):
    with sync_playwright() as p:
        browser = p.chromium.launch(headless= False) #creates the playwright object
        page = browser.new_page() # creates a new page
        page.goto("https://www.target.com/")
        page.fill(selector= "input.sc-4596e520-2.dKPRDc", value= user_item)
        page.click("button.sc-4596e520-3.eaRqyD")

        # Waits for the page to load so the program can grab the link
        page.wait_for_selector("img")  # Wait for images to appear, indicating the results have loaded
        element = page.query_selector(f"img[alt*= '{user_item}']")  # grab the html that holds the link to the product
        if element:
            # Get the image source (link to the product)
            link = element.get_attribute("src")
        else:
            link = "No image found"

        page.click(f"a:has-text('{user_item}')") #This click the item with partial match of the searched item
        price = page.inner_text("span:has-text('$')") #This return the price using partial text that matched with the $ sign

        #Grabs the product name of the page it landed on
        page.wait_for_selector("h1[data-test= 'product-title']")
        name = page.inner_text("h1[data-test= 'product-title']")
        return f"The {name} cost: {price}. You purchase the item here: {link}" #return the price of an item




one = target_search("chocolate chip cookies")
print(one)




























