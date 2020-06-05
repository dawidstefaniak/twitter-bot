import twitter, requests
from decouple import config

api = twitter.Api(consumer_key=config('APIKey'),
                  consumer_secret=config('APISecret'),
                  access_token_key=config('AccessToken'),
                  access_token_secret=config('AccessTokenSecret'))


response = requests.get("https://quotes.rest/qod")

if response.status_code == 200:
    quote = response.json()['contents']['quotes'][0]['quote']

    api.PostUpdates(quote)

    print('Quote posted: ' + quote)
else :
    print('Quote posting Error. Status code: ' + response.status_code)