# 최하위 멤버(계산이 끝난) 계산, 추천인에게 돈 전달.
# 1차. 31m 틀림. seller, amount에 여러 번 들어가면, 총합을 계산하면 안 되고, 나누어 계산해야 한다. 원단위 절사 과정이 달라지기 때문
# 2차. 1e5 * 1e4 -> 1e9 안될 것 같은데...

def solution(enroll, referral, seller, amount):
    profits = {mem:0 for mem in enroll}
    profits['-'] = 0
    refer_dict = {mem:ref for mem, ref in zip(enroll, referral)}
    
    for sell, n in zip(seller, amount):
        money = 100 * n
        while sell != '-' and money > 0:
            money_give = int(money*0.1)
            profits[sell] += money - money_give
            
            money = money_give
            sell = refer_dict[sell]

    return [profits[mem] for mem in enroll]