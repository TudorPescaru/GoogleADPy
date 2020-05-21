#! /usr/bin/env python


import requests
from bs4 import BeautifulSoup
import pandas as pd

req = requests.get('https://www.bnr.ro/Cursul-de-schimb--7372.aspx')
response = req.text
link = BeautifulSoup(response, 'html.parser')
title = link.find_all('div', attrs={'class': 'contentDiv'})

"""
<table>
    <thead>
        <tr>
            <th></th>
            <th></th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td></td>
            <td></td>
        </tr>
        <tr>
            <td></td>
            <td></td>
        </tr>
    </tbody>
</table>
"""

header = []
data_list = []
set_td = set()
html_header = ''
tbody = ''
td = ''
tr = ''
table = ''
thead = ''
for i in title:
    for tr_index in i.find_all('table'):
        for td_index in tr_index.find_all('tr'):
            td_list = []
            td = ''
            for th_index in td_index.find_all('th'):
                header.append(th_index.get_text())
                html_header += f'<th>{th_index.get_text()}</th>'
            thead = f'<thead><tr>{html_header}</tr></thead>'
            for trd_index in td_index.find_all('td'):
                td_list.append(trd_index.get_text().lstrip(' '))
                td += f'<td>{trd_index.get_text().lstrip(" ")}</td>'
            tr += f'<tr>{td}</tr>'
            data_list.append(tuple(td_list))
table = f'<table>{thead}<tbody>{tr}</tbody></table>'
# to html
with open('CursBNR_HTMLGoogle.html', 'w') as f:
    f.writelines(table)
# pandas
df = pd.DataFrame(data_list, columns=header)
# to csv 
df.to_csv('CursBNR_Google.csv')
# to excel
df.to_excel('CursBNR_ExcelGoogle.xls', sheet_name='BNR', header=header, index=0)
