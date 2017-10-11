"""
言語処理100本ノック 2015
http://www.cl.ecei.tohoku.ac.jp/nlp100/#ch1

第1章: 準備運動
09. Typoglycemia

スペースで区切られた単語列に対して，各単語の先頭と末尾の文字は残し，それ以外の文字の順序をランダムに
並び替えるプログラムを作成せよ．ただし，長さが４以下の単語は並び替えないこととする．適当な英語の文
（例えば"I couldn't believe that I could actually understand what I was reading :
 the phenomenal power of the human mind ."）を与え，その実行結果を確認せよ．
"""

import random

strings = "I couldn't believe that I could actually understand what " \
          "I was reading : the phenomenal power of the human mind ."

new_strings = ''

for word in strings.split():
    if len(word) > 4:
        first_letter = word[0]
        last_letter = word[-1]
        letters = list(word[1:-1])
        random.shuffle(letters)
        shuffled_letters = ''.join(letters)
        new_word = '{}{}{}'.format(first_letter, shuffled_letters, last_letter)
        new_strings += new_word + ' '
    else:
        new_strings += word + ' '

print(new_strings)