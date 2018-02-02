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



if __name__ == "__main__":
	filename = "Zipcodes.txt"
	inputFile = open(filename,'r')
	data = inputFile.readlines()
	for x in range(len(data)):
		data[x] = data[x].strip()
	print(data)
	