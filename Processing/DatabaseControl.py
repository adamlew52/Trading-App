import sqlite3

SiteNames = []

def getSiteData():
    #open the file containing file data
    testdata = open("ExampleSiteData.txt", "r") 
    #import data from examplesitedata.txt [change to ScrapedLinks.db later]


    siteDataArray = []

    for siteData in testdata:
        line = testdata.readline(siteData)
        for section in line:
            firstCommaLocation = line.find(',')
            secondCommaLocation = line.find(',', firstCommaLocation + 1)
            thirdCommaLocation = line.find(',', secondCommaLocation + 1)

            print("\nthe first comma location is " + firstCommaLocation)
            print("\nthe second comma location is " + secondCommaLocation)
            print("\nthe third comma location is " + thirdCommaLocation)

            SiteName = line.read(firstCommaLocation)
            url = line.read(secondCommaLocation)
            currency = line.read(thirdCommaLocation)

            print("\nthe SiteName is " + SiteName)
            print("\nthe url is " + url)
            print("\nthe currency is " + currency)

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

