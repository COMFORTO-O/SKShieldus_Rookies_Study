def calculator(a, b, op):
    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    elif op == '*':
        return a * b
    elif op == '/':
        if b == 0:
            return "0으로 나눌 수 없습니다."
        return a / b
    else:
        return "지원하지 않는 연산입니다."

user_input = input("계산식을 입력하세요 (예: 3 + 4): ")
num1, operator, num2 = user_input.split()

num1 = int(num1)
num2 = int(num2)


# 계산 후 출력
print(calculator(num1, num2, operator))
