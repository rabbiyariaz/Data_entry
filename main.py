import requests
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
from selenium import webdriver
from dotenv import load_dotenv
import os
load_dotenv()

# Headers to mimic a browser

headers = {
    'Accept-Language': 'en-PK,en-US;q=0.9,en-GB;q=0.8,en;q=0.7',

"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36"}
# Configure Chrome options and initialize WebDriver
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
chrome = webdriver.Chrome(options=chrome_options)

# Fetch the webpage
response = requests.get('https://appbrewery.github.io/Zillow-Clone/',headers=headers)
content = response.text

# Parse HTML content using BeautifulSoup
soup = BeautifulSoup(content, 'html.parser')

# Find the unordered list containing house listings
unorderedLists = soup.find_all('ul', class_='List-c11n-8-84-3-photo-cards')
if unorderedLists:
    unorderedLists = unorderedLists[0]
    house_lists = unorderedLists.find_all('li')

    # Initialize a dictionary to store house info
    dictionary_of_house_info = {}

    # Loop through each house in the list
    for case, house in enumerate(house_lists):
        house_link = house.select_one('a.StyledPropertyCardDataArea-anchor')
        address = house.select_one('address')
        price_element = house.find('span', class_='PropertyCardWrapper__StyledPriceLine')

        house_url = house_link.get('href').strip() if house_link else None
        house_address = address.text.strip() if address else None
        price_text = price_element.get_text().strip() if price_element else None

        if house_url and house_address and price_text:
            # Open Google Form using Selenium
            chrome.get(
                os.getenv("form"))

            # Collect textboxes and input data
            try:
                textboxes_list = []
                div_class = chrome.find_elements(By.CSS_SELECTOR, ".RpC4Ne.oJeWuf")
                for i in div_class:
                    textboxes_list.append(i.find_element(By.CSS_SELECTOR, ".KHxj8b.tL9Q4c"))

                # Ensure you have at least 3 fields to fill in
                if len(textboxes_list) >= 3:
                    textboxes_list[0].send_keys("San Francisco")
                    textboxes_list[1].send_keys(f"{house_address}")
                    textboxes_list[2].send_keys(f"{house_url}")

                # Click submit button
                chrome.find_element(By.CSS_SELECTOR, 'div[role=button]').click()

            except Exception as e:
                print(f"Error during form submission: {e}")

            # Store house info in dictionary for reference
            dictionary_of_house_info[case] = {
                'url': house_url,
                'address': house_address,
                'price': price_text
            }

    # Output the dictionary to verify results
    print(dictionary_of_house_info)
