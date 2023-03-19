import re
from itertools import permutations
def solution(expression):
    answer = 0
    calc = ['+','-','*']
    regex = re.compile('\d+|\D')
    _array = re.findall(regex,expression)
    _array = [int(x) if x.isdigit() else x for x in _array]

    
    for priority in list(permutations(calc,3)):
        array = _array[:]
        #print(priority)
        for calc in priority:
            stack = []
            while array: # 연산을 마칠경우
                element = array.pop(0)
                stack.append(element)
                if len(stack) >= 2:
                    if stack[-2] == calc: # 우선순위의 연산자가 나올 경우
                        if stack[-2] == '*':
                            new_value = stack[-3] * stack[-1]
                        elif stack[-2] == '+':
                            new_value = stack[-3] + stack[-1] 
                        elif stack[-2] == '-':
                            new_value = stack[-3] - stack[-1] 
                        
                        stack = stack[:-3]
                        stack.append(new_value)
            array = stack[:]
            
        result = abs(array[0])
        answer = max(result,answer)
        
    
    return answer
