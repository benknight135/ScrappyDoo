import requests
from bs4 import BeautifulSoup

class ScrappyDoo():
    def __init__(self,url):
        self.url = url
    
    def load_page(self):
        page = requests.get(self.url)
        self.soup = BeautifulSoup(page.content, 'html.parser')

    def find_element(self,element_type):
        #results = self.soup.find(id=element_id)
        results = self.soup.find_all(element_type)
        return results

if __name__ == "__main__":
    sd = ScrappyDoo("https://accessibility.umn.edu/web-designers/tables-web-pages#examples_3")
    sd.load_page()
    result = sd.find_element("table")
    for r in result:
        print(r.prettify())