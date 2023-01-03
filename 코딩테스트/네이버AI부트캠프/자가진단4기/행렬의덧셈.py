def solution(arr1, arr2):
    answer = arr1[:]

    for row in range(len(arr1)):
        for col in range(len(arr1[row])):
            answer[row][col] = arr1[row][col] + arr2[row][col] 

    return answer

if __name__ == "__main__":
    arr1 = [[1,2],[2,3]]
    arr2 = [[3,4],[5,6]]
    solution(arr1,arr2)
    pass