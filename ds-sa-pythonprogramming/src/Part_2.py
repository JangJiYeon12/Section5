"""
Bare Minimum Requirements

람다를 조건에 적합하게 활용할 줄 알아야 합니다.

요구사항:
    문제 1.
        매개변수로 들어온 리스트 요소들의 제곱수를 가지고 있는 리스트를 반환해주세요.
        단 매개변수로 들어오는 리스트는 1이상의 자연수로만 구성되어있습니다.
        람다키워드를 함수 내부에서 사용해야 합니다.
    
        *예시 1* 
            입력값:
                [1, 2, 3, 4, 5]
            출력값:
                [1, 4, 9, 16, 25]
        
        *예시 2* 
            입력값:
                [2, 4, 6, 8, 10, 12]
            출력값:
                [4, 16, 36, 64, 100, 144]
    
    문제 2.
        매개변수로 들어온 리스트 요소들이 홀수인지 짝수인지 리스트를 통해 반환해주세요.
        (반환되는 리스트 내부에는 '홀수', '짝수'만 있어야합니다.)
        단 매개변수로 들어오는 리스트는 1이상의 자연수로만 구성되어있습니다.
        람다키워드를 함수 내부에서 사용해야 합니다.

        *예시 1* 
            입력값:
                [1, 4, 9, 16, 25]
            출력값:
                ['홀수', '짝수', '홀수', '짝수', '홀수']
        
        *예시 2* 
            입력값:
                [2, 3, 6, 7, 10, 12]
            출력값:
                ['짝수', '홀수', '짝수', '홀수', '짝수', '짝수']
"""

def part2_is_square_num(a):
    ls = list(map(lambda i : i*i, a))
    
    return ls
    


def part2_is_odd_num(a):
    ls = list(map(lambda i : '홀수' if i%2 else '짝수', a))

    return ls