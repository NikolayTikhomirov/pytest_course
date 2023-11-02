# This code sample uses the 'requests' library:
# http://docs.python-requests.org
import requests
import json

url = "https://api.trello.com/1/actions/{idAction}/reactions"

headers = {
  "Content-Type": "application/json"
}

query = {
  'key': '5669faa224c7ff59d2857bff95b4ae94',
  'token': 'ATTAcf0f7d24555294cea2bf6b4c255b894c1482973aebbaba5c523976698cbb69a84F2A4B2F'
}

payload = json.dumps( {
  "shortName": "<string>",
  "skinVariation": "<string>",
  "native": "<string>",
  "unified": "<string>"
} )

response = requests.request(
   "POST",
   url,
   data=payload,
   headers=headers,
   params=query
)

print(response.text)