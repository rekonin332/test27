
money = 10

total_drink = 0
beer_price = 2

bottles_start = money/beer_price

total_drink = bottles_start
beer_cap = bottles_start
beer_bottle = bottles_start

print(total_drink)
count = 0
while beer_cap >= 4 or beer_bottle >= 2:

    if beer_cap >= 4:
        drunkThisTurn = beer_cap // 4
        consume = beer_cap // 4 * 4
        total_drink += drunkThisTurn
        beer_cap = beer_cap - drunkThisTurn * 4 + drunkThisTurn
        beer_bottle += drunkThisTurn
        print  'a .total drink: %s , bottle: %s, cap: %s, cap consume: %s' % (total_drink, beer_bottle, beer_cap, consume)

    if beer_bottle >= 2:
        drunkThisTurn = beer_bottle // 2
        consume = beer_bottle // 2 * 2
        total_drink += drunkThisTurn
        beer_bottle = beer_bottle - drunkThisTurn * 2 + drunkThisTurn
        beer_cap += drunkThisTurn
        print  'b .total drink: %s , bottle: %s, cap: %s, bottle consume: %s' % (total_drink, beer_bottle, beer_cap, consume)

    # print  'total drink: %s , bottle: %s, cap: %s' % (total_drink, beer_bottle, beer_cap)
    count += 1
    # if count > 10:
    #     break

