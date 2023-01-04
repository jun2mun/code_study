def solution(operations):
    heap = []
    answer = []
    # 명령어 구분
    for operation in operations:
        command, num = operation.split()
        if command == 'I':
            heap.append(int(num))
            heap.sort()
            pass #insert num
        elif command == 'D':
            if len(heap) == 0:
                continue
            if num == '1':
                heap.pop(-1)
                pass # 최대값 삭제
            elif num == '-1':
                heap.pop(0)
                pass # 최소값 삭제
    if len(heap) == 0:
        answer = [0,0]
    else:
        heap.sort()
        answer = [heap[-1],heap[0]]
    return answer

if __name__ == "__main__":
    operations = ["I -45", "I 653", "D 1", "I -642", "I 45", "I 97", "D 1", "D -1", "I 333"]
    print(solution(operations))
    pass