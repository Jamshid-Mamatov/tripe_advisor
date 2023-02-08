# Steps
link : response.xpath("//a[@class='Lwqic Cj b']")
name: response.xpath("//h1[@class='HjBfq']/text()").get()
location : response.xpath("//a[@class='AYHFM']/text()").get()
tel nomer : response.xpath("//a[@class='BMQDV _F G- wSSLS SwZTJ']/text()").get()
web site link in encoded format : response.xpath("//a[@class='YnKZo Ci Wc _S C AYHFM']").attrib['data-encoded-url']

next_page : response.xpath("//link[@rel='next']/@href").get()