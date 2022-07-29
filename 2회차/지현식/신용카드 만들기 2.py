start_card_numbers = ["3" ,"4", "5", "6", "9"]
for test_case in range(1, int(input()) + 1):
    word = input().split("-")
    result = ""
    flag = False
    if word[0][0] not in start_card_numbers:
        print(f"#{test_case} {0}")
        flag = True
    else:
        for i in range(len(word)):
            for j in word[i]:
                result += j
    if not flag:
        if len(result) != 16:
            print(f"#{test_case} {0}")
        else:
            print(f"#{test_case} {1}")