#!/bin/bash
# This file opens all the valid wordle words and solves each one automatically
# Takes a bit of time just fyi

File="validWordleWords.txt"
Lines=$(cat $File)
for Line in $Lines
do
	python wordleSolverTester.py $Line
done