#리스트 선언 - 여러 자료형 가능
list = [1, 1.25, 1, 'word', [1, 2, [3, 4]]]

#인덱싱
print(list[3])

print(list[4][2])   #n차원 배열처럼 리스트 내 리스트(요소)의 요소 출력 가능
print(list[4][2][0])

print(list[3][2])   #문자열도 인덱스로 값 추출 가능

#슬라이싱
print(list[2:4])
print(list[:2])     #0부터 시작할 경우 0 생략 가능

#인덱싱과 슬라이싱 중첩 사용
print(list[3][1])
print(list[3][1:3])

#연산자
list1 = [1, 2, 3]
list2 = [4, 5, 6]

print(list1 + list2)

list3 = list2 * 2 + list1
print(list3)

print(len(list3))

#변경
list4 = [1, 2, 3, [4, 5, 6]]

list4[3] = "변경"
print(list4)

#삭제
del list4[3]
print(list4)

#함수
list5 = [3, 2, 5, 1, 6, 4, 6]

list5.sort()
print(list5)

list5.reverse()
print(list5)

list5.append([77, 99])      #리스트를 요소로 추가
print(list5)

list5.extend([77, 99])      #각 요소를 리스트에 요소로 추가
print(list5)

list5.insert(3, 77)         #해당 인덱스에 값을 추가, 기존의 인덱스들은 하나씩 밀림
print(list5)

list5.remove(6)
print(list5)

list5.count(77)             #요소인 리스트 안의 요소는 count하지 않음

last = list5.pop()          #매개변수가 없는 경우 마지막 요소 pop
print(last)
print(list5)

mid = list5.pop(3)          #매개변수는 인덱스로 작용
print(mid)
print(list5)
