import requests

"""File contains function ExchangeRatePuller
    in parameters:
        - table_type- A/B/C the difference is in kind of data, ex A contains average currency
        - currency_code - 3 letters currency code (ISO 4217)
        - top_cout - max quantity of data in series
    return parameters:
        - data- dict of data of the currency requested

    addtionally functon creates a .txt by using ExportDictToTxt function 

    EX
    table_type= 'A'
    currency_code= 'USD'
    topCount='60'
    ExchangeRatePuller(table_type,currency_code,topCount)
"""
def ExchangeRatePuller(table_type, currency_code, top_count):
    url = 'http://api.nbp.pl/api/exchangerates/rates/{}/{}/last/{}/'.format(table_type, currency_code, top_count)
    response = requests.get(url)
    data = response.json()

    ExportDictToTxt('data.txt',data['rates'])

    return data


""" Function ExportDictToTxt writes input data(dict) to input file in inline order
"""
def ExportDictToTxt(file_name, data):
    with open(file_name,'w') as file:
        for counter, day in enumerate(data):
            file.write(str(data[counter])+"\n")







