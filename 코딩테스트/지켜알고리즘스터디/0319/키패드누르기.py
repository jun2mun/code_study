def solution(numbers, hand):
    answer = ''
    graph = {
        '0' : [3,1], '1' : [0,0] , '2' : [0,1] , '3' : [0,2],
        '4' : [1,0], '5' : [1,1] , '6' : [1,2] , '7' : [2,0],
        '8' : [2,1], '9' : [2,2] , '*' : [3,0] , '#' : [3,2]
    }
    left_cur = [3,0]; right_cur = [3,2]
    for number in numbers:
        if number in [1,4,7]: # 왼쪽 손가락
            left_cur = graph[str(number)]
            answer += 'L'
        elif number in [3,6,9]: # 오른쪽 손가락
            right_cur = graph[str(number)]
            answer += 'R'
        elif number in [2,5,8,0]: # 가운데 번호 경우 
            left_calc = sum(abs(graph[str(number)][idx] - left_cur[idx]) for idx in [0,1])
            right_calc = sum(abs(graph[str(number)][idx] - right_cur[idx]) for idx in [0,1])
            if left_calc == right_calc:
                answer += hand[0].upper()
                if hand[0] == 'r':
                    right_cur = graph[str(number)]
                elif hand[0] == 'l':
                    left_cur = graph[str(number)]
                    
            elif left_calc > right_calc:
                answer += 'R'
                right_cur = graph[str(number)]
            elif left_calc < right_calc:
                answer += 'L'
                left_cur = graph[str(number)]
                




    return answer