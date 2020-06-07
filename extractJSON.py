import subprocess


def extract(dataset):
    execute = ["java", "-jar", "irbench-v0.0.1-beta.2.jar", "-questions", dataset]
    return subprocess.run(execute, capture_output=True).stdout.decode()



with open('qald-8-train.json', 'w') as f:
    data = extract("qald-8-train-multilingual")
    f.write(data)


with open('qald-8-test.json', 'w') as f:
    data = extract("qald-8-test-multilingual")
    f.write(data)

