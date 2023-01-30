# 입력
N = int(input())
A = list(map(int, input().split()))
M = int(input())
arr = list(map(int, input().split()))
A.sort()			# A 정렬

# arr의 각 원소별로 이분탐색
for num in arr:
    lt, rt = 0, N - 1		# lt는 맨 앞, rt는 맨 뒤
    isExist = False		# 찾음 여부

    # 이분탐색 시작
    while lt <= rt:		# lt가 rt보다 커지면 반복문 탈출
        mid = (lt + rt) // 2	# mid는 lt와 rt의 중간값
        if num == A[mid]:	# num(목표값)이 A[mid]값과 같다면 (목표값 존재여부를 알았다면)
            isExist = True	# isExist Ture 변경
            print(1)		# 1 출력
            break		# 반복문 탈출
        elif num > A[mid]:	# A[mid]가 num보다 작으면
            lt = mid + 1	# lt를 높임
        else:			# A[mid]가 num보다 크다면
            rt = mid - 1	# rt를 낮춤

    if not isExist:		# 찾지 못한 경우
        print(0)		# 0 출력