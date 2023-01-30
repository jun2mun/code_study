from itertools import product

def solution(users,emotions):
    answer = [0,0] # 이모티콘 플러스 가입 수 , 이모티콘 매출액
    cases = [10,20,30,40]
    for case in product(cases,repeat=len(emotions)): # 완전 탐색
        total_pay = 0 # 유저가 지불 한 금액 총합
        plus_num = 0 # 플러스 가입한 사용자 수
        for rate , price in users:
            pay = 0
            for i, emotion in enumerate(emotions):
                if case[i] >= rate: # 이모티콘의 할인율(case[i]가 rate(고객의 할인율)보다 큼)
                    pay += emotion * (100-case[i]) // 100
            if pay >= price: # 이모티콘 구매를 모두 취소하고 플러스 가입
                plus_num +=1
            else: # 이모티콘  플러스 가입하지 않는 경우
                total_pay += pay
        if plus_num > answer[0]: # 이모티놐 플러스 가입자 수가 증가한 경우
            answer[0], answer[1] = plus_num, total_pay
        elif plus_num == answer[0] and total_pay > answer[1]:
            answer[1] = total_pay

    return answer


users = [[40, 10000], [25, 10000]]
emotions = [7000, 9000]
answer = solution(users,emotions)
print(f'{answer}')