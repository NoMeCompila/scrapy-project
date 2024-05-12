import requests
from bs4 import BeautifulSoup

headers = {
        'USER_AGENT': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36'
}

url = 'https://stackoverflow.com/questions'

response = requests.get(url, headers=headers)

soup = BeautifulSoup(response.text, features="lxml")

questions = soup.find(id='questions')

questions_list = questions.find_all('div', class_='s-post-summary--content')

for question in questions_list:
    title = question.find('h3').text
    print(title)