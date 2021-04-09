import random
import json

data1 = []
for item in range(0, 1000):
    gender=(random.choice(['male', 'female']))
    HeightCm=(random.randrange(150, 200))
    WeightKg=(random.randrange(60, 100))
    data1.append({"Gender": gender, "HeightCm": HeightCm, "WeightKg": WeightKg})
with open('data.json', 'w') as fp:
    json.dump(data1, fp)
