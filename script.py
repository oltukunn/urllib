#!/usr/bin/env python
#python3系
#urllib.request urlを開くための拡張可能なライブラリ

import urllib.request
filename = "master"


# with 開始と終了を必要とする処理(withを使用すると自動的に閉じる処理もする)
# open(file名,'read') as csvfile

with open("{0}.csv".format(filename), 'r') as csvfile:
    i = 0
    for line in csvfile:
        splitted_line = line.split(',')
        print(splitted_line)
        if splitted_line[1] != '' and splitted_line[1] != "\n":
            #urllib.request.urlretrieve(ダウンロードするURL,保存するファイル名)
            urllib.request.urlretrieve(splitted_line[1], splitted_line[0] + '_' + str(i) + ".jpeg")
            i += 1
        else:
            print('hello,world')