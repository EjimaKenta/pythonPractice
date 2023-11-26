
#! 通常import (import ファイルの名前 で可能)
#! code7_01をimportしたいときは import code7_01.py
import math
print(f"円周率は{math.pi}")
print(f"小数点以下切り捨てで{math.floor(math.pi)}")
print(f"小数点以下切り上げで{math.ceil(math.pi)}")
print("")

#! as文を用いたimport
import math as m
print(f"円周率は{m.pi}")
print(f"小数点以下切り捨てで{math.floor(m.pi)}")
print(f"小数点以下切り上げで{math.ceil(m.pi)}")
print("")

#! 特定の変数や関数だけを利用するfrom~構文
from math import pi
from math import floor
from math import ceil
print(f"円周率は{pi}")
print(f"小数点以下切り捨てで{floor(pi)}")
print(f"小数点以下切り上げで{ceil(pi)}")

#! pythonでは非推奨だが、ワイルドカードimportも可能 -> from ~ import *
#? 何の関数を取り込んだのか不明瞭で、上書きする可能性があるため非推奨。
