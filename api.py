import sys
import json
from cal_bmi import cal_bmi
import os
import logging as log

data1 = []


def make_logger():
    if os.path.exists(os.path.join(os.getcwd(), 'logs')) is False:
        os.makedirs(os.path.join(os.getcwd(), 'logs'))

    if os.path.exists(os.path.join(os.getcwd(), 'logs', 'logger.log')) is False:
        with open(os.path.join(os.getcwd(), 'logs', 'logger.log'), 'w') as fp:
            pass


logger_args = {
    "format": '%(levelname)s:%(asctime)s %(message)s',
    "datefmt": '%d-%m-%Y %H:%M:%S::',
    "level": log.INFO,
    "filename": "logs/logger.log"
}

make_logger()
log.basicConfig(**logger_args)


def calculate_bmi(json_data,flag):
    for data in json_data:
        gender = data['Gender']
        HeightCm = data['HeightCm']
        WeightKg = data['WeightKg']
        bmi, category, challenge = cal_bmi(HeightCm, WeightKg)

        log.info('gender , HeightCm,WeightKg is  {} ,{}, {}'.format(gender, HeightCm, WeightKg))
        log.info('bmi , category,WeightKg is  {} ,{}, {}'.format(bmi, category, challenge))
        data1.append(
            {"Gender": gender, "HeightCm": HeightCm, "WeightKg": WeightKg, 'bmi': bmi, 'category': category,
             'challenge': challenge})
        if flag:
            print('bmi is {}',bmi)
            print('category is {}',category)
            print('challenge is {}',challenge)


def overweight_person():
    count = 0

    for item in range(len(data1)):
        if (data1[item]['category']) == 'Overweight':
            count = count + 1
            log.info('overweight person details are gender={},height={},weight={},bmi={},category={},challenge={}'.format(
                data1[item]['Gender'], data1[item]['HeightCm'], data1[item]['WeightKg'], data1[item]['bmi'],
                data1[item]['category'],
                data1[item]['challenge']))
    log.info('No of overweight persions is {}'.format(count))
    return count


if __name__ == '__main__':
    '''
    input 0 if you want to calculate bmi for 1 persion 
    input 1 if you want to calculate bmi for large dataset(here data.json)
    
    '''
    type_of_input = int(sys.argv[1])
    flag=True
    if type_of_input == 0:
        #python3 api.py 0 '[{"Gender": "female", "HeightCm": 169, "WeightKg": 76}]'
        input_data = json.loads(sys.argv[2])
        calculate_bmi(input_data,flag)
    if type_of_input == 1:
        #python3 api.py 1
        f = open('data.json', )
        json_data = json.load(f)
        log.info('BMI calculation started')
        log.info('bmi function called')
        calculate_bmi(json_data,flag=False)
    no_overwieght_persions = overweight_person()
    print(no_overwieght_persions)
