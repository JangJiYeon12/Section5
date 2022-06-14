# Sprint Challenge: Python Programming

## 1번 문제 - 클래스와 리스트 컴프리헨션 (총 문제 : 8개)

- Human 클래스가 선언되어있습니다.

  - 답안작성부분 : '**#####소스코드작성#####**', '**pass**' 로 명시된 부분뿐만 아니라 tests 코드에 통과될 수 있도록 코드를 작성해주세요.

- Human 클래스에 할당된 humans object 값을 참조하여 주어진 컴프리헨션 문제를 해결합니다.

  - 모든 문제는 출력조건을 반드시 확인하여야 한다.

  ---

## 2번, 3번 문제 - 클래스와 OOP (총 문제 : 4개)

### 2) 아래 조건에 따라 기본 클래스를 작성하세요.

- 클래스를 다양하게 활용하자.

- 기능이 다양한 경우 기능별로 클래스를 구성해보자.

```python
# 조건1-1 : 아래 클래스 계층형태에 따라 클래스를 생성하는 코드를 작성하세요.
# 조건1-2 : 아래 코드에서는 개별적으로 기능이 존재하지 않는 클래스이므로 별도의 코드는 작성할 필요없습니다.
# 조건1-3 : 화살표가 의미하는 것은 모두 상속관계를 나타냅니다. (화살표관계 : [부모클래스]->[자식클래스])

# 조건1-4. 클래스 계층구조:
#
#  [Vehicle]->[FlightVehicle]->[Starship]
#      |                |
#      v                v
# [GroundVehicle]      [Airplane]
#   |       |
#   v       v
# [Car]  [Motorcycle]


###### 클래스 생성 ######
```

### 3) 아래 조건에 따라 코드를 작성하세요.

```python
# 조건1-1 : 'GroundVehicle 클래스'에서 'vroong'을 반환하는 'drive() 메소드'를 추가하세요.
# 조건1-2 : 'GroundVehicle 클래스'에서 'num_wheels 변수'의 기본값이 4가 되도록 기본 생성자 코드를 작성하세요.

class GroundVehicle:
    pass

```

```python
# 조건2-1 : 'GroundVehicle 클래스'의 서브클래스인 'Motorcycle 클래스'를 선언하세요.
# 조건2-2 : 'Motorcycle 클래스'에서 수퍼클래스를 활용하여 'num_wheels 변수' 값을 2로 설정하세요.
# 조건2-3 : 'GroundVehicle 클래스'의 'drive() 메소드'를 오버라이드하고 'Bang'을 반환하도록 하세요.


vehicles = pass
```

```python
# 조건3-1 : 위에서 선언된 클래스에 대해 '반복적으로 drive() 메소드를 출력'하는 결과를 작성하세요.

```

---

## 4번 문제 - 파이썬과 자료구조의 시간복잡도 (총 문제 : 6개)

- 주어진 코드를 분석하면서 **시간복잡도**를 알아보자
- 예제로 주어진 코드는 수정하지 않고 `#답안을 작성해주세요` 라고 표기된 부분만 수정하자 (time_complexity라는 이름이 포함된 함수만 해당)
- 답안은 소스코드 상단에 선언된 전역변수를 사용하자
---

## 5번 문제 - 🔥 도전과제 

- 도전과제의 목적 : 프로그래밍의 중요개념인 조건문과 반복문을 활용하여 문제해결능력을 상승시키자.

- 문제조건 : 주어진 점수에서 '**0점부터 100점대까지 몇 명**'이 있는지 파악할 수 있도록 코드를 작성하자. 문제에 작성되어있는 ` print("{0} 점대 - : {1} 명")`를 사용하여 0점부터 100점대까지 몇 명이 있는지 **출력하는** 코드를 작성한다

  - 추가조건1 : 점수가 마이너스인 경우 예외처리해주는 코드도 별도로 작성한다.

  - 추가조건2 : 0점이상 10점미만은 0점대이고, 10점이상 20점미만은 10점대로 소속되며 나머지 점수대도 같은 맥락으로 계산된다.

    - [N점]이상 [M점] 미만은 [N 점대]로 소속된다.

  - 아래 '예시출력값'을 확인하자.

- 예시출력값 

      0 점대 - : 2 명
      10 점대 - : 1 명
      20 점대 - : 2 명
      30 점대 - : 3 명
      40 점대 - : 4 명
      50 점대 - : 0 명
      60 점대 - : 2 명
      70 점대 - : 2 명
      80 점대 - : 1 명
      90 점대 - : 2 명
      100 점대 - : 1 명