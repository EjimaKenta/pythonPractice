
#! ディクショナリにディクショナリをネストできる
matsuda_scores = {"network":60, "database": 80, "security":50}
asagi_scores   = {"network":80, "database": 75, "security":92}
member_score = {
    "松田":matsuda_scores,
    "浅木":asagi_scores
}
print(matsuda_scores)
print(asagi_scores)
print(member_score)

#! ディクショナリにセットをネストできる
member_hobbies = {
    "松田": {"SNS", "麻雀", "自転車"},
    "浅木": {"麻雀", "食べ歩き", "数学", "数学", "数学"}
}
print(member_hobbies)
print(member_hobbies["松田"])
print(member_hobbies["浅木"]) #* 重複不可のため、数学は1つのみ表示

#! セットによる集合演算
#? セット間に「&、|、-、^」を挟むと各集合演算が可能
setA = member_hobbies["松田"]
setB = member_hobbies["浅木"]

#* 和集合 : 少なくとも片方に入っているもの
union = setA | setB
print(f"和集合:{union}")
print("")

#* 積集合 : 両方ともに入っているもの
intersection_set = setA & setB
print(f"積集合:{intersection_set}")
print("")

#* 差集合 : 片方に含まれているけれど、もう片方には含まれていないもの
difference_set = setA - setB
print(f"差集合:{difference_set}")
print("")

#* 対称差 : 両方の集合のどちらか片方だけに含まれるもの
symmetrical_difference = setA ^ setB
print(f"対称差:{symmetrical_difference}")
print("")

#! 二次元リストの例
#? 二次元リスト= リスト中にリストが入った構造
numA = [1,2,3]
numB = [4,5,6]
numC = [numA,numB]
print(numC)         #* リストC全体を参照
print(numC[0])      #* リストCの0番目（リストA）を参照
print(numC[1][2])   #* リストCの1（リストA）の2番目を参照

