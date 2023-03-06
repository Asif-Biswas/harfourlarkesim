import requests
from bs4 import BeautifulSoup
import openpyxl
from openpyxl import Workbook


# URL to scrape
url = "https://www.inecnigeria.org/collections/"

# Get the HTML
r = requests.get(url)

# Parse the HTML
soup = BeautifulSoup(r.text, "html.parser")

# Get the list (class="col-lg-3 text-center")
l = soup.find_all("div", {"class": "col-lg-3 text-center"})

for i in l:
    # Get the link 
    link = i.find("a")
    # Get the text
    text = link.text
    # Get the href
    href = link.get("href")
    # Print the text and href
    #print(text, href)
    if text != '':
        sheet = requests.get(href)
        sheet = BeautifulSoup(sheet.text, "html.parser")
        # get the div id="sheets-viewport"
        sheets_viewport = sheet.find("div", {"id": "sheets-viewport"})
        third_child = sheets_viewport.select_one("div:nth-of-type(3)")
        table = third_child.find("table")
        tbody = table.find("tbody")

        wb = Workbook()
        ws = wb.active
        
        for tr in tbody.find_all('tr'):
            tds = tr.find_all('td')
            row = [td.text for td in tds]
            ws.append(row)
        wb.save(text + '.xlsx')
        print(text + '.xlsx')
        


