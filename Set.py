#Set

#set 키워드 있는 선언
set1 = set([1, 2, 3])
set2 = set("Hello")

print(set1, set2)

#set 키워드 없는 선언
set3 = {1, 2, 3}

print(set3)

# !! 세 개는 모두 같은 set을 생성 !!
set4 = set([3, 4, 5, 6])
set5 = set({4, 5, 6})
set6 = {4, 5, 6}

print(set4, set5, set6)

#연산자
print(set1 | set4)  #합집합
print(set1 & set4)  #교집합
print(set1 - set4)  #차집합

#관련 함수
set1.add(10)
print(set1)
set1.add("Hello")               #문자열 하나면 add시 문자열 그대로 들어감

set1.update([20, 30])
print(set1)
# set1.update(40, 50)   정수 여러개 추가할 경우 리스트 형식으로 해야 함
# print(set1)
set1.update(["Hello", "Bye"])   #문자열 여러개 update시 문자열 그대로 들어감
print(set1)
set1.update("Hello")            #문자열 하나 update시 split 되어 들어감

set1.remove("Hello")
print(set1)
