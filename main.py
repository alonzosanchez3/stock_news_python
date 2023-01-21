import requests
import os

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"
aa_api_key = 'VR3AMUW4SWKADF2R'
aa_parameters = {
  "function": "TIME_SERIES_DAILY",
  "symbol": STOCK_NAME,
  "apikey": aa_api_key
}
na_api_key = '4b9f0d794d4a44fa8cd5bf35fdc471d1'
na_parameters = {
  'apiKey': na_api_key,
  'q': COMPANY_NAME,
  "pageSize": 3,
  "searchIn": 'title'

}

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

    ## STEP 1: Use https://www.alphavantage.co/documentation/#daily
# When stock price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

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

    ## STEP 2: https://newsapi.org/
    # Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME.

#TODO 6. - Instead of printing ("Get News"), use the News API to get articles related to the COMPANY_NAME.
response = requests.get(NEWS_ENDPOINT, na_parameters)
data = response.json()['articles']
articles_list = data[:3]
print(articles_list)

#TODO 7. - Use Python slice operator to create a list that contains the first 3 articles. Hint: https://stackoverflow.com/questions/509211/understanding-slice-notation




    ## STEP 3: Use twilio.com/docs/sms/quickstart/python
    #to send a separate message with each article's title and description to your phone number.

#TODO 8. - Create a new list of the first 3 article's headline and description using list comprehension.

#TODO 9. - Send each article as a separate message via Twilio.



#Optional TODO: Format the message like this:
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?.
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?.
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""