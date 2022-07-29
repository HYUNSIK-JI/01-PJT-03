for test_case in range(1, int(input()) + 1):
    numbers = [0] + list(map(int , input().split()))
    answer = [numbers[i] * 2 if i % 2 != 0 else numbers[i] for i in range(1, 16)]
    print(f"#{test_case} {0}" if not sum(answer) % 10 else f"#{test_case} {10 - sum(answer) % 10}")