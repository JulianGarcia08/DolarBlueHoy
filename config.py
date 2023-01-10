import requests

blueDollar = requests.get('https://api.bluelytics.com.ar/v2/latest').json()['blue']

blue_dollar_purchase = blueDollar.get('value_buy')

blue_dollar_sales = blueDollar.get('value_sell')

intermediate_price = blueDollar.get('value_avg')

day_of_this_price = requests.get('https://api.bluelytics.com.ar/v2/latest').json()['last_update']