email = input("이메일 주소를 입력하세요: ")

if "@" in email and "." in email:
    print("유효한 이메일 주소입니다.")
else:
    print("유효하지 않은 이메일 주소입니다.")