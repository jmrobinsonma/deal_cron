from bs4 import BeautifulSoup
from requests import get

url = "https://westernmass.craigslist.org/search/zip?hasPic=1&postedToday=1"
response = get(url)
soup = BeautifulSoup(response.text,'html.parser')
#print(soup)
posts = soup.find_all('li',class_='result-row')
#print(posts[1])
#a class="result-title hdrlnk"

for post in posts:
	post_title = post.find('a', class_='result-title hdrlnk')
	post_link = post_title['href']
	region = bool(post_link.split('/')[2].split('.')[0]=='westernmass')
	if region:
		post_title_text = post_title.text
		post_price = post.find('span', class_='result-price').text
		post_datetime = post.find('time', class_= 'result-date')['title']
		print()
		print(post_price)
		print(post_title_text)
		print(post_datetime)
		print(post_link)
		print(f"region: {region}")


















