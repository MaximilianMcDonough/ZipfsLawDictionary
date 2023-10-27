from selenium import webdriver
from bs4 import BeautifulSoup
import re
import collections
import csv

#the main methode where the program starts
def main():
	
	# making the web driver object and dictionary
	driver = webdriver.Safari()
	dictionary = dict()

	# loop that gets wikipedia pages and adds words to the dictionary
	wordCount = 0
	for i in range(10000):
		text = cleanText(getPage(driver))
		dictionary, wordCount = updateDictionary(dictionary, text.split(), wordCount)

	
	dictionary = dict(sorted(dictionary.items(), key=lambda kv:kv[1]))
	
	writeCsv(dictionary, wordCount)

	driver.close()

# methode that gets text from wikepedia
def getPage(driver):
	
	# link to random page
	NewPageLink = 'https://en.wikipedia.org/wiki/Special:Random'

	# goes to the random paage
	driver.get(NewPageLink)

	# gets the html
	html_source_code = driver.execute_script("return document.body.innerHTML;")
	soup: BeautifulSoup = BeautifulSoup(html_source_code, 'html.parser')

	# gets the text from the html
	text = ''
	for p in soup.find(id='bodyContent').find_all('p'):
		text += p.text
	
	return text

# cleans the text
def cleanText(text):
	newText = re.sub("^<(.*)>$", " ", text)

	return newText

# updates the dictionary
def updateDictionary(dictionary, text, count):
	
	for word in text:
		# all uper case to lower case
		word = word.lower()
		
		# skips words that have [,],(,),., \, in them
		if '[' in word or ']' in word or '(' in word or ')' in word or '.' in word or ',' in word:
			continue

		# updates the word counter
		count += 1
		
		# adds the word to the dictionary or adds one to the number of instances 
		if word in dictionary:
			dictionary[word] += 1

		else:
			dictionary[word] = 1

	# returns a touple dictionary and the word counter
	return (dictionary, count)

def writeCsv(dictionary, wordCount):
	with open('ZipfsLawDict.csv', 'w', newline='') as csvfile:
		fieldnames = ['Words', 'Frequency']
		writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

		writer.writeheader()
		for word in dictionary:
			print(word, dictionary[word])
			writer.writerow({'Words': word, 'Frequency': dictionary[word]/wordCount})
    	


# calls tha main function
if __name__ == '__main__':
	main()
