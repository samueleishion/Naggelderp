#!/usr/bin/python

import sys
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

def show_top_gram(title, grams): 
	print title
	i = 0
	for g in grams:
		vis = "*"*g[1] 
		print g[0]+" "+str(g[1])+" "+vis 
		i+=1
		if i==9:
			break 

	print "" 

def generate(one, two, three, limit):
	previous = ""
	letter = "<" 
	word = ""

	while(letter!=">"):
		temp = {} 
		pool = [] 
		result = []

		for k in two: 
			if string_contains(letter, k[0], 0): 
				if not k[0] in temp: 
					temp[k[0]] = 0 
				temp[k[0]] += 1 

		if letter!="<":
			for k in three: 
				if string_contains(previous, k[0], 0) and string_contains(letter, k[0], 1):
					if not k[0] in temp: 
						temp[k[0][1:]] = 0 
					temp[k[0][1:]] += 1


		for t in temp:
			pool.append((t,temp[t]))

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
		previous = letter 
		letter = result[i][0][1]  
		word += "" if letter==">" else letter 

	return word 


def main(args):
	cmd = args[1] 
	lines = load("words.txt") 
	limit = longest_length(lines) 

	onegrams = count_1_grams(lines) 
	twograms = count_2_grams(lines) 
	thrgrams = count_3_grams(lines) 

	onegrams = sorted(onegrams.items(), key=operator.itemgetter(1))[::-1]
	twograms = sorted(twograms.items(), key=operator.itemgetter(1))[::-1] 
	thrgrams = sorted(thrgrams.items(), key=operator.itemgetter(1))[::-1] 

	if cmd=="analysis":
		show_top_gram("onegrams", onegrams) 
		show_top_gram("twograms", twograms) 
		show_top_gram("thrgrams", thrgrams) 

	elif cmd=="generate":
		print generate(onegrams, twograms, thrgrams, limit) 

	else: 
		print "Please choose a valide option. "

main(sys.argv) 