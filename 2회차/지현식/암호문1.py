for test_case in range(1, 11):
    cip_len = int(input())
    cip = list(map(int, input().split()))

    command_cnt = int(input())
    command = list(input().split())

    for i in range(len(command)):
        if command[i] == "I":
            position = int(command[i + 1])
            insert_command_count = int(command[i + 2])
            for j in range(insert_command_count):
                cip.insert(position + j, int(command[i + 2 + (j + 1)]))
    print(f"#{test_case}", end=" ")
    print(*cip[:10])