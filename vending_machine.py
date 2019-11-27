from byotest import *

eur_coins = [200,100,50,20,10,5,2,1]
usd_coins = [100,50,25,10,5,1]

def get_change(amount, coins=eur_coins):
    change = []
    for coin in coins:
        while coin <= amount:
            amount -= coin
            change.append(coin)
    
    return change

test_are_equal(get_change(0), [])
test_are_equal(get_change(1), [1])
test_are_equal(get_change(5), [5])
test_are_equal(get_change(3), [2,1])
test_are_equal(get_change(7), [5,2])
test_are_equal(get_change(8), [5,2,1])
test_are_equal(get_change(9), [5,2,2])
test_are_equal(get_change(35, usd_coins), [25, 10])


print(get_change(432))
print(get_change(892))

print("All tests pass!")
