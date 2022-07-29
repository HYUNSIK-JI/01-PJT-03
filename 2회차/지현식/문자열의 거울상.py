for test_case in range(1, int(input()) + 1):
    word = input()

    answer = ""

    for i in word:
        if i == "b":
            answer += "d"
        elif i == "d":
            answer += "b"
        elif i == "p":
            answer += "q"
        else:
            answer += "p"
    print(f"#{test_case} {answer[::-1]}")