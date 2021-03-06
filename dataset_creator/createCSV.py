import json
import pandas as pd

data = []


def parseJsonData(f):
    global data
    data = []
    while (True):
        line = f.readline()
        if line == '':
            break
        parsed_json = json.loads(line)
        data.append(parsed_json)


def createCSV(name):
    global data
    questions = []
    lang = []
    for i in range(len(data)):
        item = data[i]
        questions.append(item['question'])
        lang.append(item['lang'])

    output = pd.DataFrame({'questions': questions, 'lang': lang})
    output.to_csv(name+'.csv', index=False)


if __name__ == '__main__':
    with open('qald-9-train.json', 'r') as f:
        parseJsonData(f)
    createCSV("qald-9-train")

    with open('qald-9-test.json','r') as f:
        parseJsonData(f)
    createCSV('qald-9-test')



