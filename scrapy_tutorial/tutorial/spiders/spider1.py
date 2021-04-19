
import scrapy

# Shortcut to start_requests


class QuotesSpider(scrapy.Spider):
    name = "quotes"
    start_urls = [
        'http://quotes.toscrape.com/page/1/',
        'http://quotes.toscrape.com/page/2/',
    ]
    # Latest : Extracting data in our spider

    def parse(self, response):
        for quote in response.css('div.quote'):
            yield {
                'text': quote.css('span.text::text').get(),
                'author': quote.css('small.author::text').get(),
                'tags': quote.css('div.tags a.tag::text').getall(),
            }

    #Part -2
    # def parse(self, response):
    #     page = response.url.split("/")[-2]
    #     filename = f'quotes-{page}.html'
    #     with open(filename, 'wb') as f:
    #         f.write(response.body)

# Part-1
# class QuotesSpider(scrapy.Spider):
#     name = "quotes"

#     def start_requests(self):
#         urls = [
#             'http://quotes.toscrape.com/page/1/',
#             'http://quotes.toscrape.com/page/2/',
#         ]
#         for url in urls:
#             yield scrapy.Request(url=url, callback=self.parse)

#     def parse(self, response):
#         page = response.url.split("/")[-2]
#         filename = f'quotes-{page}.html'
#         with open(filename, 'wb') as f:
#             f.write(response.body)
#         self.log(f'Saved file {filename}')
# 


# We can add Pagination , if we want & even redirect elements based on urls

# class AuthorSpider(scrapy.Spider):
#     name = 'author'

#     start_urls = ['http://quotes.toscrape.com/']

#     def parse(self, response):
#         author_page_links = response.css('.author + a')
#         yield from response.follow_all(author_page_links, self.parse_author)

#         pagination_links = response.css('li.next a')
#         yield from response.follow_all(pagination_links, self.parse)

#     def parse_author(self, response):
#         def extract_with_css(query):
#             return response.css(query).get(default='').strip()

#         yield {
#             'name': extract_with_css('h3.author-title::text'),
#             'birthdate': extract_with_css('.author-born-date::text'),
#             'bio': extract_with_css('.author-description::text'),
#         }