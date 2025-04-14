text = "Python is awesome"
str = "aeiouAEIOU"
count = 0

for char in text:
    if char in str:
        count += 1

print(f"모음의 개수는 {count}개입니다.")
