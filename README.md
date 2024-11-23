# Data_entry

## Project Overview
This script automates the process of scraping house data from a Zillow-clone webpage and submitting that data to a Google Form using Selenium. The script performs the following steps:
1. Scrapes house details (URL, address, and price) using requests and BeautifulSoup.
2. Automates filling out a Google Form using Selenium for each house.
## Requirements
### Python Libraries:
requests: For HTTP requests to fetch the webpage.
beautifulsoup4: For parsing HTML content.
selenium: For automating web interactions.
dotenv: For securely managing environment variables.
### WebDriver:
Download and install the ChromeDriver version compatible with your Chrome browser. Add it to your system's PATH or provide its path during webdriver.Chrome() initialization.
### Environment Variables:
Create a .env file in the root directory.
Add the URL of the Google Form in the .env file:

