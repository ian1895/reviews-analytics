import time
import random

data = []
count = 0
with open('reviews.txt', 'r') as f:
	for line in f:
		data.append(line)
		count += 1
		if count % 1000 == 0:
			print(len(data))
print('資料讀取完畢，總共有', len(data), '筆資料')

sum_len=0
for d in data:
	sum_len += len(d)
print('留言平均長度為: ', sum_len/len(data))	

new = []
for d in data:
	if len(d) < 100:
		new.append(d)
print('總共有', len(new), '筆留言長度小於100')

good = []
for d in data:
	if 'good' in d:
		good.append(d)
print('一共有', len(good), '筆留言提到good')		
# 上面等於下面寫法
# good = [d for d in data if 'good' in d]
# print(good)

bad = ['bad' in d for d in data]
# print(bad)
# 上面等於下面寫法
# bad = []
# for d in date:
#	bad.append('bad' in d)


# 文字計數
start_time = time.time()
wc = {} # word_count
for d in data:
	words = d.split()
	for word in words:
		if word in wc:
			wc[word] += 1
		else:
			wc[word] = 1 # add new key in wc dictionary

for word in wc:
	if wc[word] > 1000000:
		print(word, wc[word])
end_time = time.time()
print('花了', end_time - start_time, 'seconds')

while True:
	word = input('請問你想查什麼字: ')
	if word =='q':
		break
	if word in wc:
		print(word, '出現過的次數為: ', wc[word])
	else:
		print('這個字沒有出現過喔')	
print('感謝使用查詢功能')
