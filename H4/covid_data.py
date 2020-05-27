#! /usr/bin/env python

"""COVID-19 Data Table Creation FOR 3-24 April"""

from selenium import webdriver
import pandas as pd


# Initialise browser webdriver and list of urls
browser = webdriver.Chrome('/usr/local/bin/chromedriver')
urls = ["https://www.mai.gov.ro/informare-covid-19-grupul-de-comunicare-strategica-"
        + str(i) + "-aprilie-2020-ora-13-00/" for i in range(3, 25)]

# Initialise dict used to store table data
county_data = {"Nr. crt.": [str(i) + '.' for i in range(1, 44)], "Judet": []}
# Total does not need a number
county_data["Nr. crt."].append(' ')
# Counter for DAY number
DAY = 2
# Iterate through urls
for url in urls:
    DAY += 1
    # Access webpage
    browser.get(url)
    # Check if webpage contains required data
    header = browser.find_element_by_tag_name('h1')
    if header.text == "Această pagină nu există.":
        continue
    # Get table data
    table = browser.find_element_by_tag_name('table')
    t_lines = table.text.split('\n')
    county_data["Numar de cazuri confirmate " + str(DAY) + " apr"] = []

    # Iterate through lines in the table and populate dict
    for line in t_lines[1:-1]:
        # Get county name and add if not already added
        COUNTY = ''.join(line.split(' ')[1:-1]).replace('.', '. ')
        if COUNTY not in county_data["Judet"]:
            county_data["Judet"].append(COUNTY)
        # Add number of cases for county
        county_data["Numar de cazuri confirmate " + str(DAY) + " apr"].append(
            int(line.split(' ')[-1].replace('.', '')))

    # Add 0 for counties that do not exist in report
    if len(county_data["Numar de cazuri confirmate " + str(DAY) + " apr"]) < 43:
        county_data["Numar de cazuri confirmate " + str(DAY) + " apr"].append(0)

    # Add total number of cases for current DAY
    if "TOTAL" not in county_data["Judet"]:
        county_data["Judet"].append("TOTAL")
        if '–' not in county_data["Judet"]:
            county_data["Judet"].insert(-1, '–')
    county_data["Numar de cazuri confirmate " + str(DAY) + " apr"].append(
        int(t_lines[-1].split(' ')[-1].replace('.', '')))

browser.close()

df = pd.DataFrame(county_data)
# Convert to excel file
df.to_excel("COVID_DATA.xls", sheet_name="COVID", header=county_data.keys(), index=0)
# Convert to html file
df.to_html("COVID_DATA.html", header=county_data.keys(), index=0)
