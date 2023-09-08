#String
str1 = """
파이썬 연습 
연습
연습
"""
print(str1)

str2 = '''\
파이썬 복습
복습
복습\
'''
print(str2)

#포맷팅

# %버전
str3 = "%d번 버스를 타고 %s에 갈거얌" %(62, "집")
# str4 = "%s번 버스를 타고 %d에 갈거얌" %(62, "집")     알아서 형식에 맞는걸 찾아가지 않음 -> 순서가 맞아야함
print(str3)

#.format 버전
str5 = "{}원짜리 아이스크림을 {}개 사서 {}에 가야지".format(100, 10, "집")
print(str5)
str6 = "{1}원짜리 아이스크림을 {2}개 사서 {0}에 가야지".format(100, 10, "집")
print(str6)

#관련 함수
str7 = "가영이 짱짱맨"
str8 = "가영이"

len(str7)
str7.split()
# str8.split("")      #자바처럼 하나씩 나눠주진 않음 
str7.count("이")
str7.replace("짱", "뿡")
str7.find("짱") 
str7.join("!!!")  

str9 = "BaNaNa"
str9.upper()
str9.lower()


