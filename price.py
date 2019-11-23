# price_with_discount = price - price * discount / 100
# print(price_with_discount)
# def get_summ(one,two,delimiter='&'):
#     one=str(one)
#     two=str(two)
#     return '{}{}{}!'.format(one,delimiter,two)
# print(get_summ("learn","python").upper())
def format_price(price):
    price=int(price)
    return f"Цена:{price} руб."
print (format_price(56,24))
