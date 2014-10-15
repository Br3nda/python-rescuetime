import requests

"""
For api docs see https://www.rescuetime.com/anapi/setup/documentation
"""

class RescueTimeClient:
  rest_api_url = 'https://www.rescuetime.com/anapi/data.json'
  def __init__(self, key):
    self.key = key

  def select(self, **kwargs):
    kwargs['op'] = 'select'
    kwargs['key'] = self.key
    response = requests.get(self.rest_api_url, params=kwargs)
    return response.json()
