# RDBMS_IA-2
#### Name : Rishabh Kothari , Roll no :1911110
#### Class : SY COMPS B
#### Course : RDBMS
#### Faculty name : VPV Sir & PYB Ma'am

#### Topic : Implementation of Udemy_Spam_Detection_Bot using PRAW, Web Scraping using Scrapy & Beautiful Soup Web Crawling.


#### Basic Setup : Install PRAW ,Scrapy & Beautiful soup libraries using pip in terminal(if not installed).

## Part 1 :  Implementation of Udemy_Spam_Detection_Bot using PRAW

It is basically used to Detect Spam Comments on a Particular Subreddit for Udemy Courses based on a particular Z-Score.
If Z-Score >= 0.5 , It is a Spam else pass.

### To run the program (2 options):

(Option 1) : Directly open the Jupyter notebook & Run it.

(Option 2) :
1. git clone https://github.com/rishabh547/RDBMS_IA-2
2. Run the Udemy_Spam_detection_bot.py file inside Udemy_subreddit_Spam_Detection_Bot folder to see the implementation.


## Part 2 : Beautiful Soup Web Crawling
It is Basically used to scrape images from a particular subreddit & keep track of the count of images.

### To run the program : 
Just run the script.py file inside the folder Bsoup_Reddit_Web_Crawling.


## Part 3 : Scrapy tutorial.
It is basically used to scrape quotes from online urls & store them in various types of files like csv, json ,etc.

### To run the program : 
1. Open the folder scrapy_tutorial and then cd tutorial for working with spider1.py file

### Working in the scrapy shell with selectors(in root directory - scrapy_tutorial)
```
scrapy shell 'http://quotes.toscrape.com/page/1/'
```

```
response.css('title')
response.css('title').get()
response.css('title::text').get()

response.css('h3::text').get()
response.css('h3::text')[1].get()
response.css('h3::text').getall()

response.css('.post-header').get()
response.css('.post-header a').get()

response.css('p::text').re(r'scraping')
response.css('p::text').re(r's\w+')
response.css('p::text').re(r'(\w+) you (\w+)')

response.xpath('//h3')
response.xpath('//h3/text()').extract()

and so on .. (More commands can be used to scrape different kinds of data)
```
We can even scrape quotes from urls using ```scrapy crawl quotes command in tutorial directory & store them in json & csv files.```

#### Commands are:
```
scrapy crawl quotes 
scrapy crawl quotes -O quotes.json
scrapy crawl quotes -O quotes.csv 
```

### For any Help refer :
Offical Documentation of all the frameworks & libraries used in Project

PRAW : https://praw.readthedocs.io/
Beautiful Soup :https://www.crummy.com/software/BeautifulSoup/bs4/doc/
Scrapy : https://doc.scrapy.org/en/latest/intro/tutorial.html#extracting-data-in-our-spider

#### Note : All the above commands are meant for a normal python interpreter.
#### A user can create a virtualenv as well & after activating it can execute the same commands as above.

Thank you!
