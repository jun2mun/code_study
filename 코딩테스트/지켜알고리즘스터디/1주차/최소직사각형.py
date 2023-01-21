import math
def 비교(min_row,min_col,row,col):
    """
    입력값으로 들어온 가로,세로 길이 크기 비교를 통해
    가로 세로 길이 추출, 넓이 return
    """
    temp_col = min_col; temp_row = min_row
    if min_col < col:
        temp_col = col
    if min_row < row:
        temp_row = row

    temp_rect = temp_col * temp_row

    return temp_rect,temp_col,temp_row

def solution(sizes):
    answer = 0

    min_col = 0; min_row = 0; min_rect = math.inf
    for size in sizes:

        # 회전 X
        row,col = size[0],size[1]
        넓이1,가로1,세로1 = 비교(min_col,min_row,row,col)

        # 회전 O
        row,col = size[1],size[0]
        비교(min_col,min_row,row,col)
        넓이2,가로2,세로2 = 비교(min_col,min_row,row,col)

        # 가로,세로 길이 업데이트
        # 작은 넓이를 만들어내는 지갑의 가로,세로 길이, 넓이 저장
        min_rect=min(넓이1,넓이2)
        if min_rect == 넓이1:
            min_row,min_col =가로1,세로1
        if min_rect == 넓이2:
            min_row,min_col =가로2,세로2

    answer = min_rect
    return answer

if __name__ == "__main__":
    sizes = [[14, 4], [19, 6], [6, 16], [18, 7], [7, 11]]
    print(solution(sizes))
    pass