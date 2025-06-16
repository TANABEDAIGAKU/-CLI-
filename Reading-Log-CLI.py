import csv
#csvファイルを新しく生成するためにaを使用
f = open("book.csv", "a")
#簡潔にデータを入力するためにinputを使用
print("本のタイトルを入力してください")
title = input(">>")
print("本の著者を入力してください")
author = input(">>")
print("1～5の評価を入力してください")
review = input(">>")
#入力する内容を指定するためにdataを使用
data = [title,author,review]
#データを入力するためにwriterを使用
writer = csv.writer(f)
#データを入力するためにwriterowを使用
writer.writerow(data)
#ファイルを閉じるためにcloseを使用
f.close()