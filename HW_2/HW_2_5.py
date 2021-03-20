raw_prices = [57.8, 46.51, 97, 34.71, 15.09, 10, 8.37, 5.05, 7, 20.05, 00.06]
format_prices = []

for p in raw_prices:
    price_r_kk = ""
    _kk = round((p - int(p)) * 100)
    if _kk // 10 == 0:
        price_r_kk = f'{int(p):d} руб {_kk:02d} коп'
    else:
        price_r_kk = f'{int(p):d} руб {_kk:2d} коп'

    format_prices.append(str(price_r_kk))

prices_message = ", ".join(format_prices)

print(prices_message)
rp_ch = id(raw_prices)
raw_prices.sort()
print(raw_prices)
sp_ch = id(raw_prices)
print(rp_ch == sp_ch)

raw_prices_rev = list(reversed(raw_prices))
five_prices = sorted(raw_prices_rev[:5])
print(five_prices)
