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