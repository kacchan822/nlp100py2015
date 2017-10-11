"""
言語処理100本ノック 2015
http://www.cl.ecei.tohoku.ac.jp/nlp100/#ch1

第1章: 準備運動
08. 暗号文
与えられた文字列の各文字を，以下の仕様で変換する関数cipherを実装せよ．

    英小文字ならば(219 - 文字コード)の文字に置換
    その他の文字はそのまま出力

この関数を用い，英語のメッセージを暗号化・復号化せよ．
"""

def cipher(strings):
    new_strings = ''
    for s in strings:
        if ord(s) in range(ord('a'), ord('z')+1):
            new_strings += chr(219 - ord(s))
        else:
            new_strings += s
    return new_strings

def decipher(strings):
    new_strings = ''
    for s in strings:
        if 219 - ord(s) in range(ord('a'), ord('z')+1):
            new_strings += chr(219 - ord(s))
        else:
            new_strings += s
    return new_strings


cipher_string = cipher('abA')
print(cipher_string)
print(decipher(cipher_string))