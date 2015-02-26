import random 
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

def longest_length(lines):
	k = 0
	for i in lines: 
		if len(i)>k: 
			k = len(i) 

	return k

def is_end_gram(gram):
	try: 
		return gram.index(">")>=0
	except: 
		return False 
	 
def string_contains(needle, haystack, index):
	try: 
		return haystack.index(needle)==index 
	except: 
		return False 

def find_value_in_tuple_list(needle, haystack):
	for h in haystack:
		if h[0]==needle:
			return h[1]

	return 0

def generate(one, two, three, limit):
	letter = "<" 
	word = ""

	while(letter!=">"):
		pool = [] 
		result = []

		for k in two: 
			if string_contains(letter, k[0], 0): 
				pool.append((k[0],1))  

		for p in pool:
			v = p[1] + find_value_in_tuple_list(p[0],one) 
			if(is_end_gram(p[0])): 
				v *= (len(word)/limit)+1
			v *= random.uniform(0.75,0.85) 
			result.append((p[0],v)) 

		result = sorted(result, key=operator.itemgetter(1))[::-1] 

		i = 0
		# while(i<len(result)-1 and letter==result[i][0]):
		# 	i+=1
		letter = result[i][0][1]  
		word += "" if letter==">" else letter 

	return word 


def main():
	lines = load("words.txt") 
	limit = longest_length(lines) 

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

	print ""
	print generate(onegrams, twograms, thrgrams, limit) 

main() 