import requests
import os
from twilio.rest import Client


STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"
aa_api_key = 'VR3AMUW4SWK'
aa_parameters = {
  "function": "TIME_SERIES_DAILY",
  "symbol": STOCK_NAME,
  "apikey": aa_api_key
}
na_api_key = '4b9f0d794d4a44fa8cd5b'
na_parameters = {
  'apiKey': na_api_key,
  'q': COMPANY_NAME,
  "pageSize": 3,
  "searchIn": 'title'

}


STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

response = requests.get(STOCK_ENDPOINT, params=aa_parameters)
response.raise_for_status()
data = response.json()["Time Series (Daily)"]
data_list = [value for (key, value) in data.items()]
print(data_list)
yesterday_data = data_list[0]['4. close']
print(yesterday_data)

day_before_yesterday_data = data_list[1]['4. close']


difference = abs(float(yesterday_data) - float(day_before_yesterday_data))


diff_percent = (difference / float(yesterday_data)) * 100
print(diff_percent)

if diff_percent > 1:
  print('Get News')

response = requests.get(NEWS_ENDPOINT, na_parameters)
data = response.json()['articles']
articles_list = data[:3]
print(articles_list)


formatted_articles = [f"Headline: {article['title']}. \nBrief: {article['description']}" for article in articles_list]


client = Client(TWILIO_SID, TWILIO_AUTH)
for article in formatted_articles:
  message = client.messages.create(
    body=article,
    from_="+18449441591",
    to=
  )
