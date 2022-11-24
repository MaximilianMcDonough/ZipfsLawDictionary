# ZipfsLawDictionary

## Project Aim
The aim of this project is to create a dictionary of words that is ranked in order according to Zipfs law. To accomplish this, we send get request to Wikipedia asking for random pages. once we have these wiki articles, we extract the text and rank each word according to their frequency.

## How to use?
If you don’t want to run the program yourself, I included a .txt file that you can download and use, the attached file countians a mostly correct representation of Zipfs law for the English language. It's not a completely correct representation because it uses random Wikipedia pages and there were only 10,000 pages that were used to create the list attached. All that being said, it should be good enough for most applications.

## Technology Requirements
* Python 3.6.12
* Selenium 4.0
* Beautiful soup 4.9.0
