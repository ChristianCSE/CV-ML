import re
import urllib.error
import urllib.parse
import urllib.request
from bs4 import BeautifulSoup
import requests
import subprocess 

def folderDates(tags):
  re_date_main = re.compile(tags, re.DOTALL)
  return re_date_main

def retrieveURLMaterial(url):
  urlRequest  = urllib.request.Request(url) #we are requesting to open the url
  response = urllib.request.urlopen(urlRequest) #we are opening it
  page     = response.read().decode('utf-8') # we are reading the html code
  return page

kb = dict() #this is where we are storing the stuff

def getDates():
  date_entries = folderDates('<img src="/icons/blank.gif" alt="Icon ">(.+)<a href="handouts/">')
  page = retrieveURLMaterial('http://www.mathcs.emory.edu/~cs424000/share/')
  m = date_entries.search(page) # remove all irrelevant text 
  main = m.group(1)
  paritionDates = folderDates('<a href="(.+?)">')
  titles = [ (m.group(1), m.start(), m.end()) for m in paritionDates.finditer(main)]
  container = [];
  for i, title in enumerate(titles):
    curr = title[0]
    if '0' in curr and 'cs' not in curr:
      container.append(curr)
  print(container)    
  return container

def breakDateTable(url):
  re_table_date = re.compile('<table cellspacing(.+)</table>', re.DOTALL)
  currPage = retrieveURLMaterial(url)
  m = re_table_date.search(currPage)
  main = m.group(1)
  getImg = folderDates("<img width='133' height='100' style='border:0' src='(.+?)' alt='' />")
  titles = [ (m.group(1), m.start(), m.end()) for m in getImg.finditer(main)]
  # print(titles)
  finalizedPicURL = []
  for i, loggedDates in enumerate(titles):
    contURL = url + loggedDates[0]
    contURL = contURL.replace('/tn/', '/')
    # print(contURL)
    finalizedPicURL.append(contURL)
  print(finalizedPicURL)
  return finalizedPicURL

def partitionDates(datesWithTraits): 
  for i in datesWithTraits:
    url = 'http://www.mathcs.emory.edu/~cs424000/share/' + i + 'images/'
    picturesContainer = breakDateTable(url)
    # have access to one lecture day
    # now make a new subfolder and start downloading the images into that folder
    # print(picturesContainer, i)
    makePDF(picturesContainer, i)

def readURLPDF(dlURL, writeTo):
  pdfGot = urllib.request.urlopen(dlURL)
  localFile = open(writeTo, 'wb')
  localFile.write(pdfGot.read())
  pdfGot.close()
  localFile.close()

def makePDF(currentDL, o):
  name = '../lectures/'
  subFolderName = 'mkdir ' + o
  currentDL = currentDL[:len(currentDL)-1]
  subprocess.call(subFolderName, shell=True, cwd='/Users/christian/Desktop/lectures')
  counter = 0
  for currLink in currentDL:
    curr_file_name = name + str(o) + str(counter) + '.jpg'
    counter = counter + 1
    print(curr_file_name) # back out go into folder and make file
    subprocess.call(["touch", curr_file_name])
    readURLPDF(currLink, curr_file_name)

datesWithTraits = getDates()
partitionDates(datesWithTraits)