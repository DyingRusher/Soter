from re import A
import requests
from bs4 import BeautifulSoup


def getAmazonPrice(alink):
    headers1 = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36'
        }
    amazoncode=requests.get(alink,headers=headers1)
    amazonsoup=BeautifulSoup(amazoncode.content,'html.parser')
    amazonprice=amazonsoup.find('span',class_='a-price-whole')
    return amazonprice.text
    
def getFlipkartPrice(flink):
    headers1 = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36'
        }
    flipkartcode=requests.get(flink,headers=headers1)
    flipkartsoup=BeautifulSoup(flipkartcode.content,'html.parser')
    flipkartprice=flipkartsoup.find('div',class_='_30jeq3 _16Jk6d')
    return flipkartprice.text
    
    
class iPhone:
    ram=0
    rom=0
    name=''
    color=''
    amazonlink=''    
    flipkartlink=''
    amazonprice=''
    flipkartprice=''
    def __init__(self,name,color,rom,ram,amazonlink,flipkartlink):
        self.name=name
        self.color=color
        self.ram=ram
        self.rom=rom
        self.amazonlink=amazonlink
        self.flipkartlink=flipkartlink
        self.amazonprice=getAmazonPrice(amazonlink)
        self.flipkartprice=getFlipkartPrice(flipkartlink)
    
    
iphone13MiniGreen128_4=iPhone(name='Iphone 13 mini',color='green',rom=128,ram=4,amazonlink='https://www.amazon.in/Apple-iPhone-13-Mini-128/dp/B09V44LTTQ/ref=sr_1_1_sspa?crid=QFY61HHE8E5C&keywords=iphone+13&qid=1666188970&qu=eyJxc2MiOiI0LjU4IiwicXNhIjoiNC4wNCIsInFzcCI6IjMuNDQifQ%3D%3D&sprefix=iphone+13%2Caps%2C340&sr=8-1-spons&psc=1',flipkartlink='https://www.flipkart.com/apple-iphone-13-green-128-gb/p/itm18a55937b2607?pid=MOBGC9VGSU9DWGJZ&lid=LSTMOBGC9VGSU9DWGJZTOZYKQ&marketplace=FLIPKART&q=iphone+13+minu+green+128+gb+4gb&store=tyy%2F4io&spotlightTagId=BestsellerId_tyy%2F4io&srno=s_1_1&otracker=search&otracker1=search&fm=Search&iid=d994e26a-b52a-405d-9395-2b890ddd3744.MOBGC9VGSU9DWGJZ.SEARCH&ppt=sp&ppn=sp&ssid=4qdtw5lx5s0000001666189796460&qH=4bd3d812b986c4ef')
iphone13MiniStarlight128_4=iPhone(name='Iphone 13 mini',color='starlight',rom=128,ram=4,amazonlink='https://www.amazon.in/Apple-iPhone-Mini-128GB-Starlight/dp/B09G91Q79X/ref=sr_1_1_sspa?keywords=iphone%2B13%2Bmini&qid=1666204036&qu=eyJxc2MiOiI0LjMxIiwicXNhIjoiMy45OSIsInFzcCI6IjMuMjYifQ%3D%3D&sr=8-1-spons&th=1',flipkartlink='https://www.flipkart.com/apple-iphone-13-product-red-128-gb/p/itm99b5658d148b0?pid=MOBG6VF59ZFEPEBX&lid=LSTMOBG6VF59ZFEPEBX8XIKMW&marketplace=FLIPKART&sattr[]=color&sattr[]=storage&st=color&otracker=search')
iphone13MiniBlue128_4=iPhone(name='Iphone 13 mini',color='Blue',rom=128,ram=4,amazonlink='https://www.amazon.in/Apple-iPhone-Mini-128GB-Starlight/dp/B09G99NBNQ/ref=sr_1_3?crid=31M27IYQOLH9G&keywords=iphone%2B13%2Bmini&qid=1666248792&qu=eyJxc2MiOiI0LjMxIiwicXNhIjoiMy45OSIsInFzcCI6IjMuMjYifQ%3D%3D&sprefix=iphone%2B13%2Bm%2Caps%2C524&sr=8-3&th=1',flipkartlink='https://www.flipkart.com/apple-iphone-13-mini-blue-128-gb/p/itmdfa435f9c48f8?pid=MOBG6VF5FKSP3VTP&lid=LSTMOBG6VF5FKSP3VTPIVL5YV&marketplace=FLIPKART&q=iphone+13+mini&store=tyy%2F4io&srno=s_1_12&otracker=search&otracker1=search&fm=organic&iid=086f4d6f-a699-40ea-940c-65c8d1a905e5.MOBG6VF5FKSP3VTP.SEARCH&ppt=hp&ppn=homepage&ssid=h1qpvq9iww0000001666249068541&qH=9446dfb1df227290')
iphone13MiniPink128_4=iPhone(name='Iphone 13 mini',color='Pink',rom=128,ram=4,amazonlink='',flipkartlink='https://www.flipkart.com/apple-iphone-13-mini-pink-128-gb/p/itm32f5a6b2a4ea3?pid=MOBG6VF5GK7Y9AJ8&lid=LSTMOBG6VF5GK7Y9AJ8PLTZ9D&marketplace=FLIPKART&q=iphone+13+mini&store=tyy%2F4io&srno=s_1_15&otracker=search&otracker1=search&fm=organic&iid=086f4d6f-a699-40ea-940c-65c8d1a905e5.MOBG6VF5GK7Y9AJ8.SEARCH&ppt=hp&ppn=homepage&ssid=h1qpvq9iww0000001666249068541&qH=9446dfb1df227290')
iphone13MiniMidnight128_4=iPhone(name='Iphone 13 mini',color='Midnight',rom=128,ram=4,amazonlink='',flipkartlink='https://www.flipkart.com/apple-iphone-13-mini-midnight-128-gb/p/itm6fb7dc262ba8c?pid=MOBG6VF5CPAWTCBH&lid=LSTMOBG6VF5CPAWTCBHSPDPW0&marketplace=FLIPKART&q=iphone+13+mini&store=tyy%2F4io&srno=s_1_13&otracker=search&otracker1=search&fm=Search&iid=fc4c8a4e-374d-4c06-a389-4e9792bf06c6.MOBG6VF5CPAWTCBH.SEARCH&ppt=sp&ppn=sp&qH=9446dfb1df227290')
iphone13MiniProductRed128_4=iPhone(name='Iphone 13 mini',color='ProductRed',rom=128,ram=4,amazonlink='',flipkartlink='https://www.flipkart.com/apple-iphone-13-mini-product-red-128-gb/p/itm2c7e4135cf793?pid=MOBG6VF564UJVCBY&lid=LSTMOBG6VF564UJVCBYS2MHHT&marketplace=FLIPKART&q=iphone+13+mini&store=tyy%2F4io&srno=s_1_14&otracker=search&otracker1=search&fm=Search&iid=fc4c8a4e-374d-4c06-a389-4e9792bf06c6.MOBG6VF564UJVCBY.SEARCH&ppt=sp&ppn=sp&qH=9446dfb1df227290')
