n = 1260
cnt = 0

coin_list = [500, 100, 50, 10]

for coin in coin_list:
    cnt += n // coin
    n %= coin

print(cnt)
