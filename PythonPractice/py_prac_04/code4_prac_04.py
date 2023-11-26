for numsA in range(1,10):
    for numsB in range(1,10):
        multiply = numsA*numsB

        #* numsAが奇数時のみ実行、結果が50を超えた場合はprintしない
        if numsA % 2 == 1 and multiply < 50:
            print(multiply,end=" ")
    print()