#! /usr/bin/env python


from selenium import webdriver
import pandas as pd


# Initialise browser webdriver and list of urls
browser = webdriver.Chrome('/usr/local/bin/chromedriver')
urls = ["https://www.mai.gov.ro/informare-covid-19-grupul-de-comunicare-strategica-" 
         + str(i) + "-aprilie-2020-ora-13-00/" for i in range(3, 25)]

# Initialise dict used to store table data
county_data = {i: [] for i in ["Nr. crt.", "Judet", "Numar de cazuri confirmate"]}

for url in urls:
    # Access webpage
    browser.get(url)
    # Check if webpage contains required data
    header = browser.find_element_by_tag_name('h1')
    if header.text == "Această pagină nu există.":
        continue
    # Get table data
    table = browser.find_element_by_tag_name('table')
    t_lines = table.text.split('\n')
    t_head = list(county_data.keys())

    # Iterate through lines in the table and populate dict
    for line in t_lines[1:]:
        # Get county index
        ind = line.split(' ')[0]
        try:
            i = int(ind.replace('.', ''))
        except ValueError:
            continue
        if ind not in county_data[t_head[0]]:
            county_data[t_head[0]].append(ind)

        # Get county name
        county = ''.join(line.split(' ')[1:-1]).replace('.', '. ')
        if county not in county_data[t_head[1]]:
            county_data[t_head[1]].append(county)

        # Increment number of cases for given county
        while len(county_data[t_head[0]]) > len(county_data[t_head[2]]):
                county_data[t_head[2]].append(0)
        county_data[t_head[2]][i - 1] += int(line.split(' ')[-1].replace('.', ''))

browser.close()

df = pd.DataFrame(county_data)
# Convert to excel file
df.to_excel("COVID_DATA.xls", sheet_name="COVID", header=county_data.keys(), index=0)
# Convert to html file
df.to_html("COVID_DATA.html", header=county_data.keys(), index=0)
