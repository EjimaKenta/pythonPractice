
#! (1)
def int_input(intItem):
    num = int(input(f"{intItem}を入力してください>> "))
    return num

#! (2)
def calc_payment(amount, people=2):
    dnum = amount / people  #? 総額を人数で割る(端数も保持)
    pay = dnum // 100 * 100 #? 100未満切り捨て

    if dnum > pay:          #? 、元数値と比較し、小さければ100円未満があったので上乗せ
        pay = int(pay + 100)

    payorg = amount - pay * (people - 1)

    return pay,payorg

#! (3)
def show_payment(pay, payorg, peaple=2):
    print("*** 支払額 ***")
    print(f"1人あたり{pay}円({people-1}人)、幹事は{payorg}円")

#! 計算データの入力
amount = int_input("支払総額")
people = int_input("参加人数")

#! 割り勘計算
[pay,payorg] = calc_payment (amount, people)

#! 結果表示
show_payment(pay, payorg, peaple=2)


#!以下を指示通りに部品化しろって問題
"""
#! 計算データの入力
amount = int(input("支払総額？ >>"))
people = int(input("参加人数？ >>"))

#! 割り勘計算
dnum = amount / people  #? 総額を人数で割る(端数も保持)
pay = dnum // 100 * 100 #? 100未満切り捨て

if dnum > pay:          #? 、元数値と比較し、小さければ100円未満があったので上乗せ
    pay = int(pay + 100)

#! 幹事の支払い額計算
payorg = amount - pay * (people - 1)

#! 結果表示
print("*** 支払額 ***")
print(f"1人あたり{pay}円({people-1}、幹事は{payorg})")
"""