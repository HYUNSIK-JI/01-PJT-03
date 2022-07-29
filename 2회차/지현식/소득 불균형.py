for test_case in range(1, int(input()) + 1):
    n = int(input())

    income = list(map(int, input().split()))
    answer = 0
    aver = sum(income) // n
    for i in income:
        if i <= aver :
            answer += 1
    print(f"#{test_case} {answer}")