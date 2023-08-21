# N(Users) <= 100, N(Emo) <= 7
# 60m
# 아.. 할인율 단위가 10이라는 것을 못봐서 30분동안 전략을 찾지 못함.
# 경우의 수 = (할인율) ** (이모티콘 수) <= 4**7 ~ 1e4
# 이모티콘마다, 할인율마다, 구매여부 기록  [[[할인된 가격 ... 가격] 4개], ]
# itertools.product(*iterables, repeat=1)

from itertools import product

def solution(users, emoticons):
    
    # record buy
    buys = []
    for emo in emoticons:
        buy_emo = []
        for sale in [10, 20, 30, 40]:
            buy_sale = []
            emo_sale = emo*(100-sale)//100
            for user_sale, _ in users:
                if user_sale <= sale:
                    buy_sale.append(emo_sale)
                else:
                    buy_sale.append(0)
            buy_emo.append(buy_sale)
        buys.append(buy_emo)

    # calcuate cases
    candidates = []
    for sales in product([0, 1, 2, 3], repeat=len(emoticons)):
        prices = [0 for _ in range(len(users))]
        for buy, sale in zip(buys, sales):
            for i, p in enumerate(buy[sale]):
                prices[i] += p
        
        emo_plus = 0
        price = 0
        for user, p in zip(users, prices):
            if p >= user[1]:
                emo_plus += 1
            else:
                price += p
        candidates.append((emo_plus, price))

    candidates.sort(reverse=True)
    
    return candidates[0]