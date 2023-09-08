#딕셔너리 선언 -> Java의 map
dic = {
    "Hello" : 1
    , "Bye" : 2
    , 3 : "Thx"
    , 4 : "Ywc"
}

print(dic)

#추가
dic["Hola"] = 5
print(dic)

#변경
dic["Hola"] = 6
print(dic)

#삭제
del dic["Hola"]
print(dic)

#관련 함수
dic.keys()
dic.values()
dic.items()
dic.get("Hello")
"Bye" in dic
"Hola" in dic
2 in dic
dic.clear()
print(dic)