This automation project uses Python, Selenium and VS Code to create a script that scrapes data from Amazon.com and has been developed on a Windows 10 system.

NOTE: Installing and configuration of Python and VS Code is not detailed in this project. 
      - Official Python site: https://www.python.org/
      - Official Visual Studio Code site: https://code.visualstudio.com/download

> Initial Project Setup
1. Create the main folder for this project named Amazon Data Scraper.
2. Inside the Amazon Data Scraper folder, create the following three folders: input, output and scraper.
5. Open VS Code, add the following Python extensions: 
   - Python, by Microsoft.
   - Python for VS Code, by Thomas Haakon Townsend
6. To install Selenium, in VS Code, open a Terminal window, and type: pip install Selenium.
7. To install the webdriver manager, go back to the terminal, and type: pip install webdriver_manager.

> Project objective:
This project has been developed as a tool to scrape data from items shown/sold in the Today's Deals section of Amazon.com website. The script in this project reads from the input CSV file the number of pages to go through and, for the items that show a price, get the deal price, list price (sometimes shown as 'was') and description, then writes details found to the output CSV file.


