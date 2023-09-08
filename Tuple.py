#튜플 !! 값 수정, 삭제, 추가 불가 !!

#괄호 있는 튜플 선언
tuple1 = (1, 2, 3, 4)
tuple2 = (5,)

print (tuple1, tuple2)

#괄호 없는 튜플 선언
tuple3 = 5, 6, 7, 8
tuple4 = 8,
print(tuple3, tuple4)

#인덱싱
print(tuple1[3])

#슬라이싱
print(tuple1[2:4])

#연산자
print(tuple1 + tuple3)
print(tuple1*2)
print(len(tuple1 + tuple3))
