import requests
import json
from wit import data_helper
import calendar
import time

# Wit.ai's API for training the app
train_api = "https://api.wit.ai/samples?v=20170307"

# Custom Headers
train_headers = {
    "Authorization": "Bearer CQXYCLH5ZCIXF62DY3XJC33JOLXO2K5V",
    "Content-Type": "application/json"
}

# Timestamp
ts = calendar.timegm(time.gmtime())
log_name = 'log_{}.txt'.format(ts)

# Document Length
doc_length = 256

# Batch Size
batch = 10

# Read Data
data = data_helper.load_tab_files(data_file='Training_data.txt', document_length=doc_length)

train_payload = []
for idx, entry in enumerate(data):
    temp_entry = {
        "text": entry[0],
        "entities": [
            {
                "entity": "intent",
                "value": entry[1]
            }
        ]
    }

    train_payload.append(temp_entry)

    # Sending payload in batch
    if (idx+1) % batch == 0 or idx == len(data):
    # if idx < 30 and idx > 19:
        # Jsonify Payload
        train_payload_json = json.dumps(train_payload)

        r = requests.post(train_api, data=train_payload_json, headers=train_headers)

        # Printing response
        print("Data no.{} - no.{}".format(idx-batch+2,idx+1))
        print(r.text)

        # Recording Error
        if r.status_code != 200:
            file = open(log_name,"a")
            file.write("Data no.{} - no.{}".format(idx-batch+2,idx+1))
            file.write("\n")
            file.write(r.text)
            file.write("\n")
            file.close
            print("Error Recorded to Log!!")

        # Reset Training Payload
        train_payload = []

# Training Data
# train_payload = [
#     {
#         "text": "XD?",
#         "entities": [
#             {
#                 "entity": "intent",
#                 "value": "BillAmount"
#             }
#         ]
#     },
#     {
#         "text": "hahaha?",
#         "entities": [
#             {
#                 "entity": "intent",
#                 "value": "BillAmount"
#             }
#         ]
#     }
# ]

