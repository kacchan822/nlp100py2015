"""
言語処理100本ノック 2015
http://www.cl.ecei.tohoku.ac.jp/nlp100/#ch1

第1章: 準備運動
03. 円周率
"Now I need a drink, alcoholic of course, after the heavy lectures involving 
quantum mechanics."という文を単語に分解し，各単語の（アルファベットの）文字数を先頭から出現順に
並べたリストを作成せよ．
"""

strings = 'Now I need a drink, alcoholic of course, ' \
          'after the heavy lectures involving quantum mechanics.'

def replace_no_alpha(strings):
    return ''.join([s for s in strings if s.isalpha()])

result_list = [len(s) for s in map(replace_no_alpha, strings.split())]

print(result_list)