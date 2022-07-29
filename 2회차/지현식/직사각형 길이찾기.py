for test_case in range(1, int(input()) + 1):
    a, b , c = map(int,input().split())

    if a == b == c:
        print(f"#{test_case} {a}")
    elif a == b and a != c:
        print(f"#{test_case} {c}")
    elif a == c and a != b:
        print(f"#{test_case} {b}")
    elif b == c and b != a:
        print(f"#{test_case} {a}")