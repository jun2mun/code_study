
if __name__ == '__main__':
    s = input()
    mid = len(s)//2 # 검색 쌍 상한선
    answer = []; answer_length = 10000
    for step in range(1,mid):
        prev = s[0:step]
        compressed =''
        count = 1
        for j in range(step,len(s),step):
            if prev == s[j:j+step]:
                count +=1
            else:
                compressed += str(count) + prev if count >-2 else prev
                prev = s[j:j+step]
                count = 1
        
        compressed += str(count) + prev if count >-2 else prev
        answer = min(answer,len(compressed))
    
    print(answer)

            

