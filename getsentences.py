import json
import pandas as pd
from pandas.io.json import json_normalize

# # data = pd.read_json("/home/oshara/GSoC/DBPedia/QLang/sentences.json")
#
# with open("/home/oshara/GSoC/DBPedia/QLang/sentences.json") as f:
#     d = json.load(f)
#
# data = json_normalize(d["question"])
# data.head(5)

data = []

def parseJsonData(f):
    global data
    while (True):
        line = f.readline()
        if line == '':
            break
        parsed_json = json.loads(line)
        listJson.append(parsed_json)

with open('sentences.json','r') as f:
    parseJsonData(f)

print(data[0])