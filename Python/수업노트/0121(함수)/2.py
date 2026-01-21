unpacked_data = (10, 20, 30) # packed, unpacked 이름은 상관 없음
a, b, c = unpacked_data  # 변수의 개수와 요소의 개수가 같아야 함

print(a)  # 10
print(b)  # 20
print(c)  # 30

def add(x, y):
    return x + y

numbers = [10, 20]

'''
add(numbers)  # TypeError 발생
print(add(numbers))  # TypeError: add() missing 1 required positional argument: 'y'
'''

add(*numbers) # 언패킹하여 전달
sum(*numbers) # 언패킹하여 전달
print(add(*numbers))  # 30
print(sum(*numbers))  # 30


