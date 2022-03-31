from codeop import CommandCompiler
import sqlite3
import re

SiteNames = []

def getSiteData():
    #open the file containing file data
    testdata = open("ExampleSiteData.txt", "r") 
    #import data from examplesitedata.txt [change to ScrapedLinks.db later]


    siteDataArray = []

    count = 0
    for allLines in testdata:
        count = count + 1
        print("this is iteration " + str(count))
        line = testdata.readline()
        for section in line:

            commaCount = line.count(',')
            firstCommaLocation = line.find(',')
            secondCommaLocation = line.find(',', firstCommaLocation + 1)

            print("\nthe comma count is: " + str(commaCount))
            print("\nthe first comma location is: " + str(firstCommaLocation))
            print("\nthe second comma location is: " + str(secondCommaLocation))
            

            temporaryLineData = line.split(",",2)

            SiteName = temporaryLineData[0]
            url = temporaryLineData[1]
            currency = temporaryLineData[2]

            print("\nthe SiteName is " + str(SiteName))
            print("\nthe url is " + str(url))
            print("\nthe currency is " + str(currency))

            siteDataArray.append(section)

    testdata.close() 
    return siteDataArray


def addToDB(SiteName, url, currency):
    conn = sqlite3.connect('ScrapedLinks.db')
    c = conn.cursor()

    #meat and potatoes

    conn.commit()
    conn.close()

def CalculatePriority(posInstance, negInstance):
    totalScore = posInstance - negInstance
    return totalScore

def addSiteToList(SiteName):
    SiteNames.append(SiteName)


def printSiteList():
    for Names in SiteNames: 
        print(Names)

