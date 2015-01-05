#!/usr/bin/python
# .- coding: utf-8 -.
# mirc-log-merge.py
# Written by Julius Chuang (jbchuan2@illinois.edu), 2014
# Released under GPLv2

import itertools
import click

def LCS(list1, list2):

	# len(list1) by len(list2) traceback matrix
	tb = [
		[0 for _ in itertools.repeat(None, len(list2))]
		   for _ in itertools.repeat(None, len(list1))
	]
	# fill traceback matrix
	for i,j in itertools.product(range(1, len(list1)), range(1, len(list2))):
		tb[i][j] = (tb[i-1][j-1] + 1 if list1[i] == list2[j]
			else max(tb[i-1][j], tb[i][j-1])
			)
	return tb

def union(list1, list2, tb=None, i=None, j=None):
	if tb is None:
		list1 = [None] + list(list1)
		list2 = [None] + list(list2)
		tb = LCS(list1, list2)
	# allow calling without i or j
	if i is None:
		i = len(list1)-1
	if j is None:
		j = len(list2)-1
	if i == 0 or j == 0:
		return list1[1:i+1] + list2[1:j+1]
	# for matches
	elif list1[i] == list2[j]:
		return union(list1, list2, tb, i-1, j-1) + [list1[i]]
	# for non-matches
	else:
		if tb[i][j-1] > tb[i-1][j]:
			return union(list1, list2, tb, i, j-1) + [list2[j]]
		else:
			return union(list1, list2, tb, i-1, j) + [list1[i]]

@click.command()
def cli()