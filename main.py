import operator 

def load(fname):
	lines = []
	with open(fname) as f: 
		lines = f.read().splitlines() 

	for i in range(len(lines)): 
		lines[i] = "<"+lines[i].replace(" ","")+">" 

	return lines 


def count_1_grams(data):
	grams = {} 

	for d in data: 
		for i in d:
			if i=="<" or i==">":
				continue 

			if not i in grams: 
				grams[i] = 0
			grams[i] += 1 

	return grams

def count_2_grams(data):
	grams = {} 

	for d in data: 
		for i in range(len(d)): 
			k = i+1

			if k>=len(d): 
				continue 

			g = d[i]+d[k]
			if not g in grams: 
				grams[g] = 0
			grams[g] += 1 

	return grams 

def count_3_grams(data):
	grams = {} 

	for d in data: 
		for i in range(len(d)): 
			k = i+1
			j = i+2

			if j>=len(d): 
				continue 

			g = d[i]+d[k]+d[j] 
			if not g in grams: 
				grams[g] = 0
			grams[g] += 1 

	return grams 
	 

def main():
	lines = load("words.txt") 
	onegrams = count_1_grams(lines) 
	twograms = count_2_grams(lines) 
	thrgrams = count_3_grams(lines) 

	onegrams = sorted(onegrams.items(), key=operator.itemgetter(1))[::-1]
	twograms = sorted(twograms.items(), key=operator.itemgetter(1))[::-1] 
	thrgrams = sorted(thrgrams.items(), key=operator.itemgetter(1))[::-1] 

	print "onegrams"
	i = 0
	for g in onegrams:
		print g[0]+" "+str(g[1]) 
		i+=1
		if i==9:
			break 

	print "twograms"
	i = 0
	for g in twograms:
		print g[0]+" "+str(g[1]) 
		i+=1
		if i==9:
			break 

	print "thrgrams"
	i = 0
	for g in thrgrams:
		print g[0]+" "+str(g[1]) 
		i+=1
		if i==9:
			break 

main() 