# Price Feed Module
# Fetches real-time price data for XAU/USD from the OANDA API.

from oandapyV20 import API
from oandapyV20.endpoints.pricing import PricingInfo
import logging

class PriceFeed:
    def __init__(self, account_id, access_token):
        self.api = API(access_token=access_token, environment="practice")
        self.account_id = account_id

    def fetch_price(self):
        try:
            params = {"instruments": "XAU_USD"}
            r = PricingInfo(self.account_id, params=params)
            response = self.api.request(r)
            price = response['prices'][0]
            return {
                "bid": float(price['bids'][0]['price']),
                "ask": float(price['asks'][0]['price']),
                "spread": float(price['asks'][0]['price']) - float(price['bids'][0]['price']),
                "timestamp": price['time']
            }
        except Exception as e:
            logging.error(f"PriceFeedError: {e}")
            raise PriceFeedError(f"Failed to fetch price: {e}")

# Custom error for price feed
class PriceFeedError(Exception):
    pass
