#set
#Python의 기본 자료형 중 하나
#중복을 허용하지 않고 순서를 유지하지 않고 mutable한 데이터 구조
#중복 제거, 집합 연산, 빠른 조회에 사용됩

# 1. 중복을 허용하지 않는다
my_set = {1, 2, 2, 3}
print(my_set)
print(type(my_set)) 

# 2. 순서가 없다
my_set = {3, 1, 2}
print(my_set) 

# 3. immutable만 추가할 수 있다
my_set = {1, 2, (3, "김")} 
print(my_set) 

# 4. mutable은 추가할 수 없다
# my_set = {1, 2, [3, 4]} 
# print(my_set) 

# 5. set 생성1
my_set = {1, 2, 3}
# 6. set 생성2
my_list = [1, 2, 2, 3]
my_set = set(my_list)
print(my_set)  # 출력: {1, 2, 3}
# 7. set 생성3
my_set = set()
print(my_set)
print(type(my_set)) 

# set주요 메서드
# add(): 새로운 요소를 추가.
# remove(): 특정 요소를 제거 (존재하지 않으면 오류).
# discard(): 특정 요소 제거 (존재하지 않아도 오류 없음).
# 합집합: set1 | set2 또는 set1.union(set2)
# 교집합: set1 & set2 또는 set1.intersection(set2)
# 차집합: set1 - set2 또는 set1.difference(set2)
# 대칭 차집합: set1 ^ set2 또는 set1.symmetric_difference(set2)
# 부분 집합 여부: set1 <= set2 또는 set1.issubset(set2)
# 상위 집합 여부: set1 >= set2 또는 set1.issuperset(set2)
# 서로소 여부: set1.isdisjoint(set2)
# len(set): 집합의 요소 개수.
# in: 요소 존재 여부 확인.
# clear(): 모든 요소 제거.