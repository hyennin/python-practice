from repeater import repeat, once

s = input("반복할 문자를 입력하세요 : ")
n = input("반복 횟수를 입력하세요 : ")

# 특정 함수만 가지고 온 것이므로 앞에 모듈 이름 붙일 필요 X (repeater.repeat(s) X)
repeat(s, int(n))
repeat(s)
once(s)