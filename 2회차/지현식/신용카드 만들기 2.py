# import sys
# sys.stdin = open("_신용카드만들기2.txt")

# 스타트 번호로 들어가야할 번호들
start_card_numbers = ["3", "4", "5", "6", "9"]
for test_case in range(1, int(input()) + 1):
    # 입력값중 하이픈("-")으로 구분자가 있으므로 -으로 기준으로 나눔
    word = input().split("-")

    # 카드번호를 넣어줄 변수
    result = ""
    # 중복 출력을 방지 하기 위한 flag
    flag = False
    # 만약 첫 스타트 숫자가 start_card_numbers에 없다면 0으로 출력
    if word[0][0] not in start_card_numbers:
        print(f"#{test_case} {0}")
        # 중복 출력 제거를 위해 출력했다는 표시로 True로 변경
        flag = True
    # 만약 첫 스타트 숫자가 start_card_numbers에 있다면
    else:
        # 카드번호의 길이를 조사 하기 위해 result에 번호를 넣어줌
        for i in range(len(word)):
            for j in word[i]:
                result += j
    # 이미 출력 된것이 있다면 중복 출력을 제거하기 위한 조건문
    if not flag:
        # 만약 카드번호의 길이가 16이 아니면 0출력
        if len(result) != 16:
            print(f"#{test_case} {0}")
        # 만약 카드번호의 길이가 16이면 1를 출력
        else:
            print(f"#{test_case} {1}")