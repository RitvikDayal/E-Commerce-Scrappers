from bs4 import BeautifulSoup as bfs
import requests
import pandas as pd

item_dict ={
    'Name':[],
    'Price':[],
    'Ship_price':[]
    }
df = pd.DataFrame.from_dict(item_dict)

print('################################################')
print('----------Item Scrapper for Newegg.com---------')
print('################################################\n')
company = input('Enter the Company name to search Laptops:\n')
print('\n')

def store_data(name,price,ship_price):
    item_dict['Name'].append(name)
    if price.isnumeric() == False:
        price = price.replace(',','')
    item_dict['Price'].append(float(price))
    if ship_price[1:5].isnumeric():
        item_dict['Ship_price'].append(float(ship_price[1:5]))
    else:
        item_dict['Ship_price'].append(0.0)
    temp_df = pd.DataFrame.from_dict(item_dict)
    df.append(temp_df)
    print(df)



for i in range(1,2):
    
    url = "https://www.newegg.com/p/pl?d={}%20Laptops&Page={}".format(company,i)
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
        if price == "N/A":
            pass
        else:
            store_data(name, price, ship_price)





