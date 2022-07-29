for test_case in range(1, 11):
    # 원본 암호문의 길이
    cip_len = int(input())
    # 원본 암호문
    cip = list(map(int, input().split()))

    # 명령어의 개수
    command_cnt = int(input())

    # 명령어
    command = list(input().split())

    for i in range(len(command)):
        # I 단어 찾기
        if command[i] == "I":
            # I 한칸 뒤는 넣어야 할 위치 표시
            position = int(command[i + 1])

            # 몇개의 숫자들을 삽입할건지 나타나는 정수
            insert_command_count = int(command[i + 2])

            # 삽입과정
            for j in range(insert_command_count):
                # 앞에서부터 x의 위치 바로 다음에 y개의 숫자를 삽입한다.
                # position + j = x의 위치 command[i + 3] 뒤부터 삽입할 숫자들 이므로 command[i + j + 3]
                cip.insert(position + j, int(command[i + 2 + (j + 1)]))
    # 출력
    print(f"#{test_case}", end=" ")
    print(*cip[:10])