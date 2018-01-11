import requests
import json
from wit import data_helper
import csv

# Wit.ai's API for evaluating messages
train_api = "https://api.wit.ai/message"

# Custom Headers
headers = {
    "Authorization": "Bearer CQXYCLH5ZCIXF62DY3XJC33JOLXO2K5V"
}

# Document Length
doc_length = 256

# Read Data
data = data_helper.load_tab_files(data_file='Test_data.txt', document_length=doc_length)

evaluated_data = []

with open('prediction.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    csv_headers = ["Sentence", "Expected", "Predicted"]
    writer.writerow(csv_headers)

    for idx, entry in enumerate(data):
        payload = {'v': "10/01/2018",
                   'q': entry[0]
                   }

        r = requests.get(train_api, params=payload, headers=headers)
        result_json = json.loads(r.text)

        expected_label = entry[1]
        if 'intent' in result_json["entities"]:
            predicted_label = result_json["entities"]["intent"][0]["value"]
        else:
            predicted_label = ""

        entry.append(predicted_label)
        # entry[2] = predicted_label

        evaluated_data.append(entry)
        print ("Data no.{} --Predicted : {} | Expected : {}".format(idx+1, predicted_label, expected_label))

        writer.writerow(entry)