for test_case in range(1, int(input()) + 1):
    # index의 짝 홀을 더 명확하게 구분 짓게 위해 맨 앞에 0을 추가 하면서 신용카드 번호를 받음
    numbers = [0] + list(map(int , input().split()))

    # answer라는 리스트는 인덱스가 홀수이면 홀수번째 속하는 값을 두배 해주고 짝수이면 속하는 값 그대로 넣어 준 리스트이다.
    # 앞서 0이라는 값을 인덱스 0에 있기 때문에 조사 해야 할 인덱스 범위는 1 ~ 15까지 이므로 range(1, 16) 이다.
    answer = [numbers[i] * 2 if i % 2 != 0 else numbers[i] for i in range(1, 16)]
    # answer의 총합이 10으로 나눴을때 나머지가 0 이면 검증해야 할 N은 0을 출력 아니면 10 - N값 이므로 출력
    print(f"#{test_case} {0}" if not sum(answer) % 10 else f"#{test_case} {10 - sum(answer) % 10}")