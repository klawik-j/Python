import requests





"""File contains function ExchangeRatePuller
    in parameters:
        - table_type- A/B/C the difference is in kind of data, ex A contains average currency
        - currency_code - 3 letters currency code (ISO 4217)
        - topCout - max quantity of data in series
    return parameters:
        - data- dict of data of the currency requested
        
    addtionally functon creates a .txt with all data 

        EX
        table_type= 'A'
        currency_code= 'USD'
        topCount='60'
        ExchangeRatePuller(table_type,currency_code,topCount)
        """

def ExchangeRatePuller(table_type,currency_code,topCount):
    url = 'http://api.nbp.pl/api/exchangerates/rates/{}/{}/last/{}/'.format(table_type, currency_code, topCount)
    response = requests.get(url)
    data = response.json()

    with open('data.txt','w') as file:
        for counter, day in enumerate(data['rates']):
            file.write(str(data['rates'][counter]) + "\n")

    return data











