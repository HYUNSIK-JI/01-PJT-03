# 최대로 많이 나온 숫자들 카운트 하는 함수 Counter 함수를 collections 패키지에서 가지고오기
from collections import Counter

for test_case in range(1, int(input()) + 1):
    t = int(input())

    # 문제에서 같은 빈도수면 큰 수를 출력하라.
    # 큰 수를 출력하기 위해 내림 차순 정렬
    numbers = sorted(list(map(int, input().split())) , reverse=True)
    # numbers 리스트안에 있는 모든 숫자들 카운트한 데이터를 ans에 집어넣기
    ans = Counter(numbers)

    # most_common(n) 카운트가 높은 점수 와 빈도수를 내림차순으로 n개 만큼 보여줌
    print(f"#{test_case} {ans.most_common(1)[0][0]}")