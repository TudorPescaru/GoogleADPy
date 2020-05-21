#! /usr/bin/env python


from selenium import webdriver
import pandas as pd
import matplotlib.pyplot as plt

browser = webdriver.Chrome('/usr/local/bin/chromedriver')
browser.get('https://www.bnr.ro/files/xml/nbrfxrates2019.htm')
table = browser.find_element_by_xpath('//*[@id="Data_table"]')

# save as txt
with open('CursBNR_Google.txt', 'w+') as f:
    f.writelines(table.text)

table_text = table.text
table_list = table_text.split('\n')

header_len = browser.find_element_by_xpath('//*[@id="Data_table"]/table/thead/tr')
header = header_len.text.split('\n')

table_dict = {i: [] for i in header}

for j in range(len(header)):
    for i in range(len(header) + int(j), len(table_list), len(header)):
        if '-' in table_list[i]:
            table_dict[header[int(j)]].append(table_list[i])
        else:
            table_dict[header[int(j)]].append(float(table_list[i]))

# print(table_dict)
df = pd.DataFrame(table_dict)
df.to_excel("BNR_ALL_VALUES_GOOGLE.xls")

browser.close()

a = header[3:9]
c = []
for i in range(3, 9):
    c.append(table_dict[header[int(i)]][int(i)])
d = sum(c)
e = []
for item in c:
    e.append(round(item/d*100))

colors = ['r', 'y', 'g', 'b', 'g', 'y']

plt.pie(e, labels=a, colors=colors, startangle=90, shadow=True,
         explode=(0.1, 0.1, 0.1, 0.1, 0.1, 0.2), radius=1.2, autopct='%1.1f%%')
plt.legend()
plt.show()
