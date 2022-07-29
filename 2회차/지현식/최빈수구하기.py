from collections import Counter

for test_case in range(1, int(input()) + 1):
    t = int(input())

    numbers = sorted(list(map(int, input().split())) , reverse=True)
    ans = Counter(numbers)

    print(f"#{test_case} {ans.most_common(1)[0][0]}")