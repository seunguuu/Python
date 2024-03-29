'''왕실의 나이트'''

input_data = input()

row = int(input_data[1])
# ord() : 아스키코드 값 출력
column = int(ord(input_data[0])) - int(ord('a')) + 1

# 8 x 8, column : abcdefgh, row : 12345678
# 나이트가 이동할 수 있는 8가지 방향 정의
# UDLR 문제에 있었던 dx, dy 변수의 기능을 steps가 수행
steps = [(1, 2), (-1, -2), (-1, 2), (1, -2), (2, 1), (-2, -1), (-2, 1), (2, -1)]

# 8가지 방향에 대하여 각 위치로 이동이 가능한지 확인
count = 0
for step in steps:
    # 이동하고자 하는 위치 확인
    next_row = row + step[0]
    next_column = column + step[1]

    # 해당 위치로 이동이 가능하다면 카운트 증가
    if next_row >= 1 and next_row <= 8 and next_column >= 1 and next_column <= 8:
        count += 1


print(count)