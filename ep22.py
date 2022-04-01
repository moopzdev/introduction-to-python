# Cash Change Machine App
amount = int(input("Show me the money: "))

if amount >= 1000:
    print(" 1000 bill : ", amount // 1000)
    amount %= 1000
if amount >= 500:
    print(" 500 bill :", amount // 500)
    amount %= 500
if amount >= 100:
    print(" 100 bill :", amount // 100)
    amount %= 100
if amount >= 50:
    print(" 50 bill :", amount // 50)
    amount %= 50
if amount >= 20:
    print(" 20 bill :", amount // 20)
    amount %= 20
if amount >= 10:
    print(" 10 coin :", amount // 10)
    amount %= 10
if amount >= 5:
    print(" 5 coin :", amount // 5)
    amount %= 5
if amount >= 2:
    print(" 2 coin :", amount // 2)
    amount %= 2
if amount >= 1:
    print(" 1 coin :", amount // 1)
    amount %= 1
