# import sys
# sys.stdin = open("_문자열의거울상.txt")

for test_case in range(1, int(input()) + 1):
    word = input()

    answer = ""
    # 거울을 만났을때 각각 b = d , p = q 로 대칭되므로 각각의 단어를 만났을때 반대 단어를 넣어야함
    for i in word:
        if i == "b":
            answer += "d"
        elif i == "d":
            answer += "b"
        elif i == "p":
            answer += "q"
        else:
            answer += "p"
    # 반대 단어를 다 넣은 answer에 순서를 바꿔주면 거울에 비친 문자열이 된다.
    print(f"#{test_case} {answer[::-1]}")