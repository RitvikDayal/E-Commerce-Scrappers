from bs4 import BeautifulSoup as bfs
import requests

print('################################################')
print('----------Item Scrapper for Newegg.com---------')
print('################################################\n')
company = input('Enter the Company name to search Laptops:\n')

url = "https://www.newegg.com/p/pl?d={}%20Laptops&Page=1".format(company)


response = requests.get(url)
data = response.text
soup = bfs(data, 'html.parser')

items = soup.find_all('div',{'class':'item-info'})

for item in items:
    name = item.find('a',{'class':'item-title'}).text
    price_tag = item.find('li',{'class':'price-current'})
    price = price_tag.find('strong').text + price_tag.find('sup').text if price_tag else "N/A"
    ship_price_tag = item.find('li',{'class':'price-ship'})
    ship_price = ship_price_tag.text if ship_price_tag else "None"
    print('Name:- {}\nPrice:- ${}\nShipping Price:- {}\n--------------'.format(name,price,ship_price))
