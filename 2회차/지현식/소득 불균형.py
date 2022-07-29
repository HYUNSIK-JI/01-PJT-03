# import sys
# sys.stdin = open("_소득불균형.txt")

for test_case in range(1, int(input()) + 1):
    n = int(input())

    # 소득들을 리스트 화
    income = list(map(int, input().split()))
    answer = 0
    # 소득들의 평균
    aver = sum(income) // n
    for i in income:
        # 만약 각각의 소득중 평균보다 작은지 비교 조건문
        if i <= aver:
            # 작으면 +1
            answer += 1
    print(f"#{test_case} {answer}")