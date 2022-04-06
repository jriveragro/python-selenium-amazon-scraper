### Import all necessary selenium, webdriver and other libraries/modules to handle the actions being
### performed by the scraper.
from distutils.spawn import find_executable
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import pandas as pd
import csv
from selenium.webdriver.common.keys import Keys
import time

data = [] 
itemsDF = pd.DataFrame(data)

### From the input file, read the number of pages to go through in the Today's Deals section.
with open('input//input_numberOfPages.csv', 'r') as inputFile:
    inputContent = csv.reader(inputFile)
    for line in inputContent:
        numberOfPages = line[0]

### Instantiate a variable and assign it the chromeoptions class from the webdriver in order to 
### have chrome specific methods and capabilities available.
optns = webdriver.ChromeOptions()

### For this example, I am adding an argument to the chromeoptions variable to ignore certification 
### errors in case they come up when the web browser is launched.
optns.add_argument('--ignore-certificate-errors')

### Using the webdriver module, I instantiate a variable, must people use 'driver', which will represent
### the chrome web browser that I will be interacting with, here, I am also telling the driver to install 
### the chromedriver from the chromeDriverManager through the service parameter. In addition, I pass the chrome options.
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=optns)

### Since 'driver' now represents my web browser, I tell it to maximize window size when it launches.
driver.maximize_window()

### Navigate to the Amazon website.
driver.get('https://www.amazon.com/')

### Click on the See all deals link.
driver.find_element(By.LINK_TEXT, 'Today\'s Deals').click()

### Get the list of buttons to navigate from page to page.
### The Next button is the last button in the list.
buttonsContainerSelector = 'div[class="a-text-center notranslate"]'
buttonsContainer = driver.find_element(By.CSS_SELECTOR, buttonsContainerSelector)
buttonsList = buttonsContainer.find_elements(By.TAG_NAME, 'a')
nextButton = buttonsList[-1]

### Use the number taken from the input file to loop through the pages in the Deals.
### NOTE: Remember that the landing page on the Deals section is page #1.
for page in range(1, int(numberOfPages)+1):
    ### Find and get the container that holds the deals in the page.
    mainDealsContainerSelector = 'div[data-testid="grid-deals-container"]'
    mainDealsContainer = driver.find_element(By.CSS_SELECTOR, mainDealsContainerSelector)

    ### Find and get each of the individual deal containers.
    dealContainer = 'div[data-testid="deal-card"]'
    dealCards = mainDealsContainer.find_elements(By.CSS_SELECTOR, dealContainer)

    ### Instantiate two a variables and assign them the selector with which the price and description of the item will be found.
    itemPricesSelector = 'span[class="a-price-whole"]'
    itemDescriptionSelector = 'div[class*="DealContent-module"]'
     
    for deal in dealCards:
        itemDescription = deal.find_element(By.CSS_SELECTOR, itemDescriptionSelector) 
        spans = deal.find_elements(By.CSS_SELECTOR, itemPricesSelector)
        if len(spans) == 2:
            ### Instantiate a list where pricess will store temporarily.

            prices = [] 
            for span in spans:
                ## Create a list of the items being scraped.
                prices.append(span.text)

            data.append([prices[0], prices[1], itemDescription.text])

    ### Click on the next button.
    nextButton.click()
                
### Close browser.
driver.close()