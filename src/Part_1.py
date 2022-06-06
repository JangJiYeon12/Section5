"""
Bare Minimum Requirements

파이썬의 기본형태를 이해하고 컴프리헨션을 활용할 줄 알아야 합니다.

요구사항:
    리스트 컴프리헨션 개념을 적용하여 '1~100까지 7과 5의 공배수' 를 구하는 코드를 작성하세요.
    아래 예시입력값과 출력값을 참조하며 문제를 해결해봅니다.

    입력값:
        없음
    출력값:
        [35, 70]
"""

def part1():
    answer = [i for i in range(1, 100) if i%35==0]

    return answer
