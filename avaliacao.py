import pandas as pd

ex1 = pd.read_excel('SiteList.xlsx')
ex2 = pd.read_excel('Results.xlsx')

merged_data = pd.merge(ex1, ex2, on=['Site ID', 'Site Name', 'Year', 'Equipment'])

resultado = merged_data[['Site ID', 'Site Name', 'Year', 'State', 'Equipment', 'Signal (%)', 'Quality (0-10)', 'Mbps']]

resultado.to_excel('quality-report-2023.xlsx', index=False)

ordenacao = pd.read_excel('quality-report-2023.xlsx')

dadosOrdenados = ordenacao.sort_values(by='State')

dadosOrdenados.to_excel('quality-report-2023.xlsx', index=False)



























