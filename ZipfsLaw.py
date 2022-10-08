from selenium import webdriver
from bs4 import BeautifulSoup
import re
import collections

def main():
	driver = webdriver.Safari()
	dictionary = dict()

	wordCount = 0
	for i in range(10000):
		text = cleanText(getPage(driver))
		text = text
		dictionary, wordCount = updateDictionary(dictionary, text.split(), wordCount)

	
	print(dict(sorted(dictionary.items(), key=lambda kv:kv[1])))
	print('number of words total words: ', wordCount)
	print('number of unique words: ', len(dictionary))

	driver.close()

def getPage(driver):
	NewPageLink = 'https://en.wikipedia.org/wiki/Special:Random'

	driver.get(NewPageLink)

	html_source_code = driver.execute_script("return document.body.innerHTML;")
	soup: BeautifulSoup = BeautifulSoup(html_source_code, 'html.parser')

	
	text = ''
	for p in soup.find(id='bodyContent').find_all('p'):
		text += p.text
	
	return text

def cleanText(text):
	newText = re.sub("^<(.*)>$", " ", text)

	return newText

def updateDictionary(dictionary, text, count):
	for word in text:
		word = word.lower()
		if '[' in word or ']' in word or '(' in word or ')' in word or '.' in word or ',' in word:
			continue

		count += 1
		if word in dictionary:
			dictionary[word] += 1

		else:
			dictionary[word] = 1

	return (dictionary, count)


main()
'''
text = 'And you were dead in the trespasses and sins 2 in which you once walked, following the course of this world, following the prince of the power of the air, the spirit that is now at work in the sons of disobedience— 3 among whom we all once lived in the passions of our flesh, carrying out the desires of the body[a] and the mind, and were by nature children of wrath, like the rest of mankind.[b] 4 But[c] God, being rich in mercy, because of the great love with which he loved us, 5 even when we were dead in our trespasses, made us alive together with Christ—by grace you have been saved— 6 and raised us up with him and seated us with him in the heavenly places in Christ Jesus, 7 so that in the coming ages he might show the immeasurable riches of his grace in kindness toward us in Christ Jesus. 8 For by grace you have been saved through faith. And this is not your own doing; it is the gift of God, 9 not a result of works, so that no one may boast. 10 For we are his workmanship, created in Christ Jesus for good works, which God prepared beforehand, that we should walk in them.'

dictionary = dict()
dictionary, count = updateDictionary(dict(),text.split(),0)

print(dict(sorted(dictionary.items(), key=lambda kv:kv[1])))
'''
