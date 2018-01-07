import requests
import json

# Wit.ai's API for training the app
train_api = "https://api.wit.ai/samples?v=20170307"

# Insert Code to Read Data

# Training Data
train_payload = [
    {
        "text": "XD?",
        "entities": [
            {
                "entity": "intent",
                "value": "BillAmount"
            }
        ]
    },
    {
        "text": "hahaha?",
        "entities": [
            {
                "entity": "intent",
                "value": "BillAmount"
            }
        ]
    }
]

# Jsonify Payload
train_payload_json = json.dumps(train_payload)

# Custom Headers
train_headers = {
    "Authorization" : "Bearer CQXYCLH5ZCIXF62DY3XJC33JOLXO2K5V",
    "Content-Type" : "application/json"
}

r = requests.post(train_api, data = train_payload_json, headers=train_headers)

# Printing response
# Might want to do response checking here
print(r.text)
