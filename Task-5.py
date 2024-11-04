import requests
from bs4 import BeautifulSoup

url = 'https://example.com'

response = requests.get(url)

if response.status_code == 200:

    soup = BeautifulSoup(response.text, 'html.parser')


    page_title = soup.title.string
    print(f"Page Title: {page_title}")


    paragraphs = soup.find_all('p')
    for para in paragraphs:
        print(para.text)


    links = soup.find_all('a')
    for link in links:
        href = link.get('href')
        text = link.get_text()
        print(f"Link: {text}, URL: {href}")
else:
    print(f"Failed to get the webpage. Status code: {response.status_code}")
