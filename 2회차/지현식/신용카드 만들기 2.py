start_card_numbers = ["3" ,"4", "5", "6", "9"]
for test_case in range(1, int(input()) + 1):
    word = input().split("-")
    result = ""
    flag = False
    for i in range(len(word)):
        for j in range(len(word[i])):
            if i == 0 and j == 0 and word[i][j] not in start_card_numbers:
                print(f"#{test_case} {0}")
                flag = True
            else:
                result += word[i][j]
    if not flag:
        print(f"#{test_case} {0}" if len(result) != 16 else f"#{test_case} {1}")