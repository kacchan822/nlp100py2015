"""
言語処理100本ノック 2015
http://www.cl.ecei.tohoku.ac.jp/nlp100/#ch1

第1章: 準備運動
06. 集合
"paraparaparadise"と"paragraph"に含まれる文字bi-gramの集合を，それぞれ, XとYとして求め，
XとYの和集合，積集合，差集合を求めよ．さらに，'se'というbi-gramがXおよびYに含まれるかどうかを調べよ．
"""

strings1 = 'paraparaparadise'
strings2 = 'paragraph'

def ngram(n, strings):
    i = 0
    result_list = []
    while i <= len(strings) - n:
        result_list.append(strings[i:i+n])
        i += 1
    return result_list

X = set(ngram(2, strings1))
Y = set(ngram(2, strings2))

print(X)
print(Y)
print(X | Y)
print(X & Y)
print(X - Y)
print('se' in X)
print('se' in Y)