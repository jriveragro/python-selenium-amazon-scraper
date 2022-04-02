### Import all necessary selenium and webdriver libraries to handle the actions being
### performed by the scraper.
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time

### Declare a variable and assign to it the path where chrome driver is located.
### srvc = 'C:\\Users\\Jesus\\Dev\\Python\\Data Scraper\\amazon\\drivers\\chromedriver.exe'

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
driver.find_element_by_link_text('Today\'s Deals').click()

### Get the container that holds the deals in the page.
selector = 'div[data-testid="grid-deals-container"]'
dealsContainer = driver.find_element(By.CSS_SELECTOR, selector)

### Print-out the count of deals in the page
selector1 = 'div[data-testid="deal-card"]'
dealCards = dealsContainer.find_elements(By.CSS_SELECTOR, selector1)

print(f'Showing a total of {len(dealCards)} items in the first page')

### Close browser.
driver.close()