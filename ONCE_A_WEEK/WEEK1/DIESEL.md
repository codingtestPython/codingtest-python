# 첫째 마당 소감
### [1주차: 코딩 테스트 사전 준비](https://hsteve.notion.site/1-120bb48f75b880949dffeb570beacedd)
- 코테 준비
    - 방법
        1. 기록하라(어디까지 생각해봤는지 우선 기록해두기)
        2. 시험 보듯 공부하라ㅠ
        3. 짧은 시간 공부해서는 절대 코딩 테스트를 통과할 수 없다ㅠㅠ
        4. 나만의 언어로 요약하라
    - 문제 분석
        1. 문제를 `동작 단위로` 쪼개서 분석
        2. `제약사항` 고려(테스트 케이스 추가 연습)
        3. 입력값 분석(`시간복잡도` 결정)
        4. `핵심 키워드 파악`
        
        ![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/afda5b93-b10b-45e9-ba6e-c3956955e3c5/f08c7f75-4554-4ced-9b0b-bea8b8f72b77/image.png)
        
        1. `데이터 흐름`이나 구성 파악
            - 데이터 삽입/삭제 빈번 → heap 자료구조
            - 데이터 50개 미만, 입력값 정리 난 → 하드코딩
            - 데이터값 격차 큰 경우 → 데이터값 인덱스 활용 지양
    - Peudo code 설계
        - Peudo code: 프로그래밍 언어 작성 지양(자연어), 자유형식
        - Peudo code 작성
            1. 세부 구현 지양. 동작 중심 작성
            2. 문제 해결 순서로 작성
            3. 충분히 테스트
- 알고리즘 효율
    - 시간복잡도(time complexity)
        - 입력 데이터 크기에 대한 연산 횟수의 상한(낮을 수록 좋다)
        - 점근적 표기법: 입력 크기를 N으로 일반화하여 연산 횟수 추이 표현
        - `빅오 표기법`(Big-o notation): 모든 경우의 알고리즘을 처리해야 하므로 보통 최악의 경우 문제 처리하는 시간복잡도로 판단
            - 최고차항으로 판단
            - f(x) = 2x^2 + 3x + 5라면, 시간복잡도는 O(x^2)으로 표현
            - f(X) = 2^x의 경우, O(2^x)
            - 제한시간이 1초인 문제 시간복잡도
                
                
                | 시간복잡도 | 최대 연산 횟수 |
                | --- | --- |
                | O(N!) | 10 |
                | O(2^N) | 20~25 |
                | O(N^3) | 200~300 |
                | O(N^2) | 3000~5000 |
                | O(N * logN) | 100만 |
                | O(N) | 1000만~2000만 |
                | O(logN) | 10억 |
- 필수 문법
    - 빌트인 데이터 타입(Built-in data type)
        - int(정수형), float(부동소수형), 문자열
        - 정수형
            - 변수 선언(a=1, b=2)
            - 산술 연산(a+b, a-b, a*b, a/b, a//b, a%b, -a, abs(-a), a**b)
            - 비교 연산(a==b, a !=b, a>b, a<b, a>=b, a<=b)
            - 비트 연산(a&b, a|b, a^b, ~a, `a<<2`, `a>>1`)
            - 논리연산(a and b, a or b, not a)
        - 부동소수형
            - 사칙연산, 나누기/모듈러/제곱
            - 논리연산 예: x > y and y < z
            - sys.float_info.epsilon
    - 컬렉션 데이터 타입
        - list, tuple, set, dict
        - 변경할 수 있는 객체(Mutable Object)
            - list, dict, set
        - 변경할 수 없는 객체(immutable Object)
            - 정수, 부동소수점, 문자열, tuple
        - List
            - 인덱싱(indexing)
            - 슬라이싱(slicing)
        - Dict
            - my_dict={ }
            my_dict[”apple”]=1
            print(my_dict) ⇒ {”apple” : 1}
            - Dict 검색
            if key in my_dict:
                value=my_dict[key]
                print(f’{key} : {value})
            else:
                print(f’{key}는 존재하지 않음)
    - 함수
        - def라는 예약어 사용하여 정의
        - lambda
        add = lambda x, y : x+y
        print(add(5,4)
        - map
    - 코드 구현
        - 조기  반환(early return)
        - 보호 구문(guard clauses)
        - 합성 함수(composite method)
        
- 후기
    - 이제 시작인데..일단 화이팅!!