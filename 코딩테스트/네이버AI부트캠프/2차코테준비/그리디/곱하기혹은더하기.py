
if __name__ == '__main__':
    S = list(map(int,input())) # 0~9 숫자로 이루어진 문자열

    answer = max(S[0]+ S[1], S[0]*S[1])
    for idx in range(2,len(S)):
        answer = max(answer*S[idx],answer+S[idx])
    
    print(answer)
