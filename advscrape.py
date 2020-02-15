import os, sys
from lxml import etree

def scrape(filename):
    print("Scraping " + filename)
    parse = etree.HTMLParser()
    tree = etree.parse(filename, parse)
    print(str(tree))


if len(sys.argv) == 1:
    files = os.scandir()
    scrapable = []
    for file in files:
        if "lADV-" in file.name:
            scrapable.append(file.name)

    print("Choose an Advocate Portal File by number:")
    for file in scrapable:
        i=0
        print("[" + str(i) + "]" + ": "+ str(scrapable[i]))
        i+=1

    choice = input("Enter the number only: ")
    choice = int(choice)
    scrape(str(scrapable[choice]))

elif len(sys.argv) == 2:
    print (str(len(sys.argv)) + " arguments detected")
    for i in sys.argv:
        print (str(i) + " " + str(type(i)))

    if "lADV-" in sys.argv[1]:
        scrape(str(sys.argv[1]))
    
else:
    print("Usage: \n advscrape \n advscrape pathtohtmlfile")