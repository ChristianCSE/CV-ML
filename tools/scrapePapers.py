#scrape papers from Dr. Fei-Fei Li  
import re
import urllib.error
import urllib.parse
import urllib.request
from bs4 import BeautifulSoup
import requests
import subprocess 
# installing packages in python3 
# use sudo pip3

# pdf source 
sourceURL = 'http://vision.stanford.edu/'

def storage():
  tags = "<td align='center' valign='top'(.+)<img width='133' height='100' style='border:0'"
  RE_CLASSES_MAIN = re.compile(tags, re.DOTALL)
  return RE_CLASSES_MAIN

def retrieveURLMaterial(url):
  urlRequest  = urllib.request.Request(url) #we are requesting to open the url
  response = urllib.request.urlopen(urlRequest) #we are opening it
  page     = response.read().decode('utf-8') # we are reading the html code
  return page


kb = dict() #this is where we are storing the stuff
# page = retrieveURLMaterial('http://www.mathcs.emory.edu/~cs424000/share/0111/images/');
page = retrieveURLMaterial('http://vision.stanford.edu/publications.html')


# m = RE_CLASSES_MAIN.search(page)

# main = m.group(1)

def rips():
  using = '<div class="plinks">(.+)>PDF</a></div>'
  prevUsed = '<div class="plinks">(.+)PDF</a></div>'
  #'<a href="(.+)">PDF'
  RE_PAPERS = re.compile(using, re.DOTALL)
  return RE_PAPERS
# print(page)

re_papers = rips()
m = re_papers.search(page)
main = m.group(1)

# print(main)

#re_paper_names = re.compile('<a href="(.+?)">PDF</a></div>', re.DOTALL)
re_paper_names = re.compile('<a href="(.+?)">PDF', re.DOTALL)

titles = [ (m.group(1), m.start(), m.end()) for m in re_paper_names.finditer(main)]
container = [];
for i, title in enumerate(titles): 
  embeddedPDF = 'pdf/'
  embeddedDoc = 'document/'
  trailingPDF = '.pdf'
  curr = title[0]
  ignores = '<div'
  # or embeddedDoc in curr or trailingPDF in curr:
  if ignores not in curr and (embeddedPDF in curr or embeddedDoc in curr or trailingPDF in curr):
    container.append(curr)

def readURLPDF(dlURL, writeTo):
  pdfGot = urllib.request.urlopen(dlURL)
  localFile = open(writeTo, 'wb')
  localFile.write(pdfGot.read())
  pdfGot.close()
  localFile.close()

# print(container)
o = 0
name = '../CVPDF/'
for partialURL in container:
  currentDL = sourceURL + partialURL
  o = o + 1
  print(currentDL)
  getContent = requests.get(currentDL)
  curr_file_name = name + str(o) + '.pdf'
  print(name)
  subprocess.call(["touch", curr_file_name])
  readURLPDF(currentDL, curr_file_name)






