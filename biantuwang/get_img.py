import requests
from lxml import etree
url = 'http://pic.netbian.com/4kdongman/index_2.html'

header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3928.4 Safari/537.36'
}

res = requests.get(url,headers=header).content.decode('gbk')
e = etree.HTML(res)
img_urls = e.xpath('//ul[@class="clearfix"]/li/a/biantuwang/@src')
img_names = e.xpath('//ul[@class="clearfix"]/li/a/b/text()')


for img_url,img_name in zip(img_urls,img_names):
    img_url = 'http://pic.netbian.com' + img_url
    res_img = requests.get(img_url,headers=header)
    name = ''.join(img_name.split()) + '.jpg'
    with open('image/'+name,'wb') as f:
        f.write(res_img.content)


