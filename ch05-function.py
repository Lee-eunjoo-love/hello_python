#. 함수 정의 (매개변수: 함수 정의시 함수 내부에 입력 받는 변수, 반환값: 함수 실행시 return 으로 내보내는 함수 결괏값)
def add(a, b):
    c = a + b
    return c

result = add(10, 20) #. 함수 호출 (인자: 함수를 호출할 때 넣는 값으로 인자로 전달한 값은 매개변수가 받아 저장)
print(f"add(10, 20) -> {result}")

def multiply_by_two(n):
    return n * 2

def add_numbers(a, b):
    return a + b

print(f"multiply_by_two(add_numbers(3, 2)) -> {multiply_by_two(add_numbers(3, 2))}") #. (3 + 2) * 2 = 10

def calculator(a, b, operator):
    if operator == "+":
        return a + b
    elif operator == "-":
        return a - b
    elif operator == "*":
        return a * b
    elif operator == "/":
        try:
            return a / b
        except ZeroDivisionError:
            return "0으로 나눌 수 없습니다."
    else:
        return "지원하지 않는 연산자입니다."
    
print("---------- calculator ----------")
print(calculator(10, 5, "+"))
print(calculator(10, 5, "-"))
print(calculator(10, 5, "*"))
print(calculator(10, 5, "/"))
print(calculator(10, 0, "/"))
print(calculator(10, 0, "@"))
