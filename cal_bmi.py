def cal_bmi(height, weight):
    height_m = height / 100
    bmi = round(weight / (height_m * height_m), 2)
    if bmi >= 40:
        return bmi, 'Very severely obese', 'Very high risk'
    if 35 <= bmi <= 39.9:
        return bmi, 'Severely obese', 'High risk'
    if 30 <= bmi <= 34.9:
        return bmi, 'Moderately obese', 'Medium risk'
    if 25 <= bmi <= 29.9:
        return bmi, 'Overweight', 'Enhanced risk'
    if 18.5 <= bmi <= 24.9:
        return bmi, 'Normal weight', 'Low risk'
    if bmi == 18.4:
        return bmi, 'Underweight', 'Malnutrition risk'
    else:
        return bmi, 'NA', 'NA'
