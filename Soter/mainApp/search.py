import requests
from bs4 import BeautifulSoup

# taking input
vs = input("Enter what you to search:")
vswords = vs.split()
# making amazon link
amazonlink = "https://www.amazon.in/s?k="
p = 1
for words in vswords:
    if(p == 1):
        amazonlink += words
        p = 0
    else:
        amazonlink += "+" + words
        
# print(amazonlink)
# making flipkart link
flipkartlink = "https://www.flipkart.com/search?q="
p = 1
for words in vswords:
    if(p == 1):
        flipkartlink += words
        p = 0
    else:
        flipkartlink += "+" + words
# print(flipkartlink)

def top5Product(alink, flink):
    headers1 = {'User-Agent':
            'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36',
            'Accept-Language': 'en-US, en;q=0.5'}
    amazoncode = requests.get(alink, headers=headers1)
    print(amazoncode)
    amazonsoup = BeautifulSoup(amazoncode.content, 'html.parser')
    aAllText = amazonsoup.find_all(
        'span', class_='a-size-medium a-color-base a-text-normal')
    aAllPrice = amazonsoup.find_all('span', class_='a-price-whole')
    aAllPicLink = amazonsoup.find_all('img', class_='s-image')
    aAllProductlink = amazonsoup.find_all(
        'a', class_='a-link-normal s-underline-text s-underline-link-text s-link-style a-text-normal')
    print("\n+++++++++++++++++++++++ 5 results in amazon: ++++++++++++++++++++++++++++++++++\n")
    for i in range(5):
        print(aAllText[i].text)
        print(aAllPrice[i].text)
        print('link of img is:', aAllPicLink[i]['src'], sep=' ')
        print('link of product is:', 'www.amazon.in',
              aAllProductlink[i]['href'], sep='')
    flipkartcode = requests.get(flink, headers=headers1)
    flipkartsoup = BeautifulSoup(flipkartcode.content, 'html.parser')
    fAllText = flipkartsoup.find_all('a', class_='s1Q9rs')
    fAllPrice = flipkartsoup.find_all('div', class_='_30jeq3')
    fAllPicLink = flipkartsoup.find_all('img', class_='_396cs4')
    fAllProductlink = flipkartsoup.find_all('a', class_='_8VNy32')
    print("\n+++++++++++++++++++++++ 5 results in flipkart: ++++++++++++++++++++++++++++++++++\n")
    # print(fAllText[0].text,"\n")
    for i in range(5):
        print(fAllText[i].text)
        print(fAllPrice[i].text)
        print('Link of pic is:', fAllPicLink[i]['src'], sep='')
        print('Link of Product:',"https://" ,'www.flipkart.com',
              fAllProductlink[i]['href'], sep='')


top5Product(amazonlink, flipkartlink)
