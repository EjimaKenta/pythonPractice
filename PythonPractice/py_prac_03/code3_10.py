print("全問にy or n で回答")
has_money = input("所持金に余裕？　y/n >> ")

#! 無駄にコメントでifをブロック分けしてやる ぐへへ…
#! >>>>>>>>>>>>>>> if-1 op
if has_money == 'y':
    is_hungry = input("飢餓？　y/n >> ")
    is_drink = input("飲酒願望？　y/n >> ")

    #? >>>>>>>>>>>>>>> if-2 op
    if is_hungry == "y" and is_drink == "y":
        print("提案: 焼肉")
    elif is_hungry == "y":
        print("提案: カレー")
    elif is_drink == "y":
        print("提案: 焼鳥")
    else:
        print("提案: パスタ")
    #? <<<<<<<<<<<<<<< if-2 ed
    is_night_snack = input("夜食は必要？　y/n >> ")

    #* >>>>>>>>>>>>>>> if-3 op
    if is_night_snack == "y":
        print("提案: コンビニチキン")
    #* <<<<<<<<<<<<<<< if-3 ed

else:
    print("提案: 自炊")
#! <<<<<<<<<<<<<<< if-1 ed