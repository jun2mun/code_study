
if __name__ == '__main__':
    S = list(map(int,input())) # 0과 1로만 이루어진 문자열 S -> 1,000,000
    zero = 0; one = 0
    
    if S[0] == 0:
        zero +=1
    elif S[0] == 1:
        one +=1
    for idx in range(len(S)-1):
        if S[idx] != S[idx+1] and S[idx+1] == 0:
            zero +=1

        elif S[idx] != S[idx+1] and S[idx+1] == 1:
            one +=1

    answer = min(one,zero)
    print(answer)