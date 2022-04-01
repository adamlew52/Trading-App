import sqlite3
import re
from urllib.error import URLError

def getSiteData():
    #open the file containing file data
    testdata = open("ExampleSiteData.txt", "r") 
    #import data from examplesitedata.txt [change to ScrapedLinks.db later]

    lineCounter = 0

    siteDataArray = []
    
    for lineCount in testdata:
        #print("TEST FLAG - current line: ", lineCounter)

        rawLineData = lineCount.strip()
        lineData = rawLineData.split(',', 3)
        
        lineCounter += 1

        
        attributeCounter = 0

        #test flags, remove later
        #print("\nLine data: ", lineData[attributeCounter])
        #print("length of lineData: ", len(lineData[attributeCounter]))

        siteDataArray.append(lineData)
        #print("FLAG - recent data appendage added to siteDataArray: ", lineData)
        attributeCounter += 1
    
    #print("\n\nFLAG - siteDataArray:\n" ,siteDataArray)

    yRef = 0
    for names in siteDataArray:
        siteNames = siteDataArray[yRef][0]
        yRef += 1  
    
    yRef = 0
    for webpage in siteDataArray:
        url = siteDataArray[yRef][1]
        yRef += 1  
    
    yRef = 0
    for coinName in siteDataArray:
        currency = siteDataArray[yRef][2]
        yRef += 1  

    #print("Total number of lines is: " , lineCounter)

    testdata.close() 

    return siteDataArray


def addToDB(siteDataArray):
    conn = sqlite3.connect("ADCP.db")
    c = conn.cursor()
    
    #Parse and add the SiteName
    yRef = 0
    for names in siteDataArray:
        siteNames = siteDataArray[yRef][0]
        print("SiteNames contents: ", siteNames)
        yRef += 1  

    #Parse and add the url

    yRef = 0
    for webpage in siteDataArray:
        url = siteDataArray[yRef][1]
        print("url contents: ", url)
        yRef += 1  
    
    #Parse and add the currency
    yRef = 0
    for coinName in siteDataArray:
        currency = siteDataArray[yRef][2]
        print("currency contents: ", currency)
        yRef += 1  
    
    c.execute('''CREATE TABLE IF NOT EXISTS 'Test Info Storage 2' (
        Article_Name TEXT,
        URL TEXT,
        Currency_Name TEXT)''')

    c.execute("INSERT INTO 'Test Info Storage 2' VALUES (?,?,?)", (siteNames,url,currency))

    conn.commit()
    conn.close()

def CalculatePriority(posInstance, negInstance):
    totalScore = posInstance - negInstance
    return totalScore




