from django.shortcuts import render
import requests
from bs4 import BeautifulSoup

# Create your views here.s
def home(request):
    return render(request, "index.html")

def search(request):
    
    if request.method == "POST":
        item = request.POST["Item"]
        vs = item
        vswords = vs.split()
                
        amazonlink = "https://www.amazon.in/s?k="
        p = 1
        for words in vswords:
            if(p == 1):
                amazonlink += words
                p = 0
            else:
                amazonlink += "+" + words
        headers1 = {'User-Agent':
            'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36',
            'Accept-Language': 'en-US, en;q=0.5'}
        amazoncode = requests.get(amazonlink, headers=headers1)
        print(amazoncode)
        amazonsoup = BeautifulSoup(amazoncode.content, 'html.parser')
       
        
        aAllText = amazonsoup.find_all(
            'span', class_='a-size-medium a-color-base a-text-normal')
        aAllPrice = amazonsoup.find_all('span', class_='a-price-whole')
        aAllPicLink = amazonsoup.find_all('img', class_='s-image')
        aAllProductlink = amazonsoup.find_all(
            'a', class_='a-link-normal s-underline-text s-underline-link-text s-link-style a-text-normal')
        
        aDict={
            'atext':[],
            'aprice':[],
            'apic':[],
            'alink':[]
        }
        
        for  i in range(0,5):
            aDict['atext'].append(aAllText[i].text)
            # print(aAllText[i].text)
            aDict['aprice'].append(aAllPrice[i].text)
            # print(aAllPrice[i].text)
            aDict['apic'].append(aAllPicLink[i]['src'])
            # print('link of img is:', aAllPicLink[i]['src'], sep=' ')
            
            # print('link of product is:', 'www.amazon.in',
                # aAllProductlink[i]['href'], sep='')
            alink="https://www.amazon.in"
            alink+=aAllProductlink[i]['href']
            aDict['alink'].append(alink)
        
        flipkartlink = "https://www.flipkart.com/search?q="
        p = 1
        for words in vswords:
            if(p == 1):
                flipkartlink += words
                p = 0
            else:
                flipkartlink += "+" + words

        headers1 = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36'
        }

        flipkartcode = requests.get(flipkartlink, headers=headers1)
        flipkartsoup = BeautifulSoup(flipkartcode.content, 'html.parser')
        fAllText = flipkartsoup.find_all('div', class_='_4rR01T')
        fAllPrice = flipkartsoup.find_all('div', class_='_30jeq3 _1_WHN1')
        fAllPicLink = flipkartsoup.find_all('img', class_='_396cs4')
        fAllProductlink = flipkartsoup.find_all('a', class_='_1fQZEK')
        
        fDict={
            'ftext':[],
            'fprice':[],
            'fpic':[],
            'flink':[]
        }
        
        # a=fAllText[4].text
        # print(a)
        for i in range(0,5):
            fDict['ftext'].append(fAllText[i].text)
           # print(fAllText[i].text)
            fDict['fprice'].append(fAllPrice[i].text)
            #print(fAllPrice[i].text)
            fDict['fpic'].append(fAllPicLink[i]['src'])
           # print('Link of pic is:', fAllPicLink[i]['src'], sep='')
            fprolink="https://www.flipkart.com"
            fprolink+=fAllProductlink[i]['href']
           # print('Link of Product:', 'https://www.flipkart.com',
            #fAllProductlink[i]['href'], sep='')
            fDict['flink'].append(fprolink)
        print(fDict)
        
        return render(request, "search.html", context = {"aDict": aDict,"fDict":fDict})
    
    return render(request,"search.html")
