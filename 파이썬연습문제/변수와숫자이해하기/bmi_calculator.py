weight = float(input("체중 입력: "))
height_cm = float(input("키 입력: "))

height_m = height_cm / 100
bmi = weight / (height_m ** 2)

print(f'BMI는 {bmi :.2f}입니다.')
