#!/bin/bash
File="validWordleWords.txt"
Lines=$(cat $File)
for Line in $Lines
do
	python wordleSolverTester.py $Line
done