import csv
import json
import webbrowser
import collections
import unittest
import sys
import glob
import os
import re
import operator






def parse(inputString, finalDict):
	
	entryParts = inputString.split(" : ")


	key = entryParts[0].strip()
	finalDict[key] = {}
	finalDict[key]['Date'] = (entryParts[1].strip())
	finalDict[key]['Asin'] = (entryParts[2].strip())
	finalDict[key]['Name'] = (entryParts[3].strip())

	finalDict[key]['Address'] = entryParts[4].split(",")[1].strip("\n").strip()
	return finalDict





if __name__ == "__main__":
	filename = "Zipcodes.txt"
	finalDict = {}
	inputFile = open(filename,'r')
	data = inputFile.readlines()#Stores each line as an entry into the array data
	for x in data:
		finalDict = parse(x,finalDict)

	
	


	