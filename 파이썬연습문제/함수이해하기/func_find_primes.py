def find_primes(start, end):
    prime = []
    for i in range(start, end):
        if i < 2:
            continue
        for j in range(2, i):
            if i % j == 0:
                break
        else:
            prime.append(i)
    return prime            

start_input = int(input("시작 값을 입력하세요: "))
end_input = int(input("끝 값을 입력하세요: "))

print("소수 리스트:", find_primes(start_input, end_input))
