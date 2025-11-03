#. 리스트: 하나의 변수로 여러 값을 저장하며 자료형으로 대괄호로 표현하며 추가/수정/삭제 가능.
student = ["홍길동", "김철수", "이영희", "전우치"]
print(student[-1], student[-2], student[-3], student[-4])
print(student[1:3]) # 끝 인덱스 미만까지(student[1], student[2])
print(student[:3]) # student[0], student[1], student[2]
print(student[2:]) # student[2], student[3]

fruit = ["사과", "배", "포도"]
print(student + fruit)
print(fruit * 3)
print("포도" in fruit)
print("딸기" in fruit)
print("오렌지" not in fruit)

fruit.append("오렌지")
fruit.remove("배")
del(fruit[0])
print(fruit)

print(len(fruit))
print(sorted(fruit, reverse=True)) # 정렬된 새로운 리스트 반환
print(fruit) # 원본 리스트는 변경되지 않음
fruit.sort() # 원본 리스트 정렬
print(fruit)
print(fruit.index("포도"))

#. 튜플: 리스트처럼 하나의 변수로 여러 값을 저장하며 자료형으로 소괄호로 표현하며 추가/수정/삭제 불가. 리스트보다 가볍고 빠르며 불변값을 보관하는데 적합.
tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)

print(tuple1 + tuple2)
print(tuple1 * 3)
print(tuple1[0], tuple1[1], tuple1[2])
print(tuple1[1:3])
print(len(tuple1))
#. tuple1.append(5) # 튜플은 변경 불가
#. tuple1[0] = 5 # 튜플은 변경 불가
#. tuple1.remove(2) # 튜플은 변경 불가

product = "샴푸,후추,치약,물티슈,설탕"
shopping = product.split(",")
print(sorted(shopping))