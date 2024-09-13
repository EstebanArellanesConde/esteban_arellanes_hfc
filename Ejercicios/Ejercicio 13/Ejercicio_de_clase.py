#!/usr/bin/python3

import requests

response = requests.get(
    "" #url
    params={"q": "language:python", "sort": "stars", "order":"desc"}
)

json_response = response.json()


{}


