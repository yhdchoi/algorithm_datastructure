# Q1
n, k = map(int, input().split())

result = 0

while True:
    # n이 k로 나누어 떨어지는 수가 될 때까지 빼기 (소수점은 버려짐 => target = 16)
    target = (n // k) * k
    print("1: " + str(target))

    result += (n - target)
    print("2: " + str(result))

    n = target
    print("3: " + str(n))

    # n이 k보다 작을때 (더 이상 나눌 수 없을 때) 반복문 탈출
    if n < k:
        break
    # k로 나누기
    result += 1
    print("4: " + str(result))
    n //= k
    print("5: " + str(n))

# 마지막으로 남은 수에 대하여 1씩 빼기
# result += (n - 1)
print("정답: " + str(result) + "번")

# 시간복잡도 logN