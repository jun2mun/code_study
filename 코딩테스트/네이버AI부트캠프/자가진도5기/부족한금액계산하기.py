def solution(price, money, count):
    answer = -1
    
    total = price * ( count * (count + 1) /2 ) 
    
    answer = money - total
    if answer >= 0:
        answer = 0
        return answer
    else:
        return abs(answer)