import sys 

length = 3

if len(sys.argv) > 1:
	length = int(sys.argv[1])

def ngrams(words, n, sep=" "):
    return [sep.join(words[i:i+n]) for i in range(len(words)-n+1)]

tg = {}

for line in sys.stdin.readlines():
	x = line.strip().split(' ')
	for n in ngrams(x, length):
		if n not in tg:
			tg[n] = 0
		tg[n] += 1

tgs = [(i[1], i[0]) for i in tg.items()]
tgs.sort(reverse=True)
for t in tgs:
	print('%d\t%s' % (t[0], t[1]))
