import scrapy
import base64

class RestaurantSpider(scrapy.Spider):
    name = "restaurant"
    allowed_domains = ["tripadvisor.com"]
    start_urls = ["https://www.tripadvisor.com/Restaurants-g32655-Los_Angeles_California.html"]

    def parse(self, response):
        
        for link in response.xpath("//a[@class='Lwqic Cj b']/@href").getall():
           
            yield scrapy.Request(response.urljoin(link), self.additional_page)
        
        next_page=response.xpath("//link[@rel='next']/@href").get()
        
        if next_page is not None:
            
            yield response.follow(next_page,callback=self.parse)

    
    def additional_page(self,response):
        
        yield{
            "name": response.xpath("//h1[@class='HjBfq']/text()").get(),
            "location" : response.xpath("//a[@class='AYHFM']/text()").get(),
            "tel_nomer" : response.xpath("//a[@class='BMQDV _F G- wSSLS SwZTJ']/text()").get(),
            "restaurant_link":base64.b64decode(response.xpath("//a[@class='YnKZo Ci Wc _S C AYHFM']/@data-encoded-url").get())[4:-4]
        }
