import sys
sys.setrecursionlimit(10**6)
import math
class _answer(object):
    def __init__(self):
        self.value = math.inf

def solution(a,candy,idx,total):
    cnt = 0
    while True:
        if idx >= len(friends): # 개수 다 채우면 total 반환
            if candy != 0: # 캔디 안쓰고
                return
            a.value = min(a.value,total)
        if candy == 0: # 캔디 다 쓰면 total 반환
            return
        if cnt > friends[idx]: # 요구한 캔디보다 더 부여하는 경우
            break # 더 많은 캔디를 넣을 수 없기에 이후 재귀문은 없앰.
        elif cnt > candy: # 부여할 수 있는 캔디보다 커지는 경우
            break
        else:
            # 리스트(idx)에 0개 넣는 경우부터 전부 다 넣는 경우 계산      
            solution(a,candy-cnt,idx+1,total + cnt**2) # candy 개수 update / idx 업데이트
            cnt +=1

    pass

if __name__ == '__main__':
    M , N = map(int,input().split())
    friends = []; total =0
    for _ in range(N):
        friend = int(input())
        friends.append(friend)
        total += friend
    
    # 아래는 부족해지는 캔디 개수를 리스트마다 할당
    # 부족해지는 캔디 개수가 요구한 캔디 개수보다 많아질 수는 없음.
    # 필요한 정보 : 요구 캔디 리스트
    a = _answer()
    solution(a,total-M,0,0)
    print(a.value)
    pass
