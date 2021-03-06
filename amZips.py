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
import requests


google_api_key = "AIzaSyD3cn_utAfFePi70-Ay1KFI9_QgA7VFckI"
googleBaseUrl = "https://maps.googleapis.com/maps/api/geocode/json"


#Because I am storing date as a number this a function you can use it back to turn it back into
#a string of the normal format "month/day/year"

def getRequest(address):
	req = requests.Request(method = 'GET', url =googleBaseUrl,params ={'address': address, 'key':google_api_key} )
	prepped = req.prepare()
	response = requests.Session().send(prepped)
	jsonResponse  =json.loads(response.text)
	if 'status' in jsonResponse:
		if jsonResponse['status'] == "ZERO_RESULTS":
			return(10000,10000)
	lat = jsonResponse['results'][0]['geometry']['location']['lat']
	lng = jsonResponse['results'][0]['geometry']['location']['lng']
	return (lat,lng)

def putBackDate(dateNum):
	dateString = str(dateNum)
	year = dateString[0:4]
	month = dateString[4:6]
	day = dateString[6:]
	return (month + "/" + day + "/" + year)

#Turns the date into a number of the format (Year)(Month)(Day)
def processDate2(dateArray):
	if(len(dateArray[0]) == 1):
		dateArray[0] = "0"+dateArray[0]
	if(len(dateArray[1]) == 1):
		dateArray[1] = "0"+dateArray[1]

	return int(dateArray[2]+dateArray[0]+dateArray[1])

#Turns the date into a number of the format (Year)(Month)(Day)
def processDate(dateArray):
	if(len(dateArray[1]) == 1):
		dateArray[1] = "0"+dateArray[1]
	if(len(dateArray[2]) == 1):
		dateArray[2] = "0"+dateArray[2]

	return int(dateArray[0]+dateArray[1]+dateArray[2])




#Parses the entries from ZipCodes.txt into a dictionary
def parse(inputString, finalDict):
	
	entryParts = inputString.split(" : ")


	key = entryParts[0].strip()
	finalDict[key] = {}

	tempDate = entryParts[1].strip().split("-")

	finalDict[key]["Original"] = inputString.strip()
	finalDict[key]['Date'] = processDate(tempDate)
	finalDict[key]['Asin'] = (entryParts[2].strip())
	if finalDict[key]['Asin'] == "null":
		finalDict[key]['Name'] = "Ashwin"
		finalDict[key]['Address'] = entryParts[3].split(",")[1].strip("\n").strip()
	else:
		finalDict[key]['Name'] = (entryParts[3].strip())
		finalDict[key]['Address'] = entryParts[4].split(",")[1].strip("\n").strip()

	

	return finalDict





if __name__ == "__main__":
	#filename = "Zipcodes.txt"
	filename = "2017to2018ZC.txt"
	finalDict = {}
	inputFile = open(filename,'r')
	data = inputFile.readlines()#Stores each line as an entry into the array data
	for x in data:
		finalDict = parse(x,finalDict)



#################UNCOMMENT ONE OR THE OTHER#########################################
	#Getting inputs from the command line arguments for now because its Faster
	startingDate = str(sys.argv[1])
	endingDate = str(sys.argv[2])
	ASIN  = str(sys.argv[3])

	#Getting inputs from the user straight up from typing (Uncomment this and comment above one if you want it)
	#startingDate = input("Enter a Starting Date (month/day/year): ")
	#endingDate = input("Enter a Ending Date (month/day/year): ")
	#ASIN  = input("Enter a ASIN: ")

	startDateArray = startingDate.split("/")
	endingDateArray = endingDate.split("/")
	#Process dates in case they are misformated for turning into a number
	startNum  = processDate2(startDateArray)
	endNum  = processDate2(endingDateArray)
	searchDictionary = {}
	for x in finalDict:
		if finalDict[x]["Asin"] == ASIN:
			if finalDict[x]["Date"] >= startNum and finalDict[x]["Date"] <= endNum:
				searchDictionary[x] = finalDict[x]
	
	#Output Query results to queryResults.txt
	resultsFile = open("queryResults.txt","w+")
	counter= 0
	for y in searchDictionary:
		#print(searchDictionary[y]["Address"])
		lat,lng = getRequest(searchDictionary[y]["Address"])
		if lat == 10000:
			continue
		resultsFile.write(str(lat) + "," + str(lng) + "\n")
		#resultsFile.write(searchDictionary[y]["Address"] + "\n")
	totalResults = len(searchDictionary)
	print("You had " + str(totalResults) + " results")





#	print(searchDictionary)


	


	
	


	