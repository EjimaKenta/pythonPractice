
#! コレクション型の相互変換 (キャスト可ということ)
scores = {"network":60, "database":80, "security":60} #*ディクショナリ
members = ["松田","浅木","工藤"] #* リスト

print(tuple(members))       #? リストのタプル化
print(list(scores))         #? scoresの"キー"のみリスト化
print(set(scores.values())) #? scoresの"値"をセット化

#! ディクショナリ変換は複雑
#? {"人名":年齢, ･･･} でディクショナリ化 (人名にはmembersを流用)
ages = (21,26,31) #* セット
print(dict(zip(members,ages)))