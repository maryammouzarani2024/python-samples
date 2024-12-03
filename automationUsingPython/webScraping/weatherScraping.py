import requests
from bs4 import BeautifulSoup
from time import sleep

def parse_single_url():
    url="https://openlibrary.org/subjects/accessible_book#ebooks=true"

    response=requests.get(url, headers={"Accept":"text/html"})
    parsed_response=BeautifulSoup(response.text, "html.parser")

    # print(parsed_response.prettify())

    authors=parsed_response.find_all("a", {"title":"See more books by, and learn about, this author"})



    for author in authors:
        print(author.text)


def parse_multiple_urls():

    base_url="https://openlibrary.org/authors/OL21976A/Patricia_Cornwell?page="
    for page_number in range(1,2):

        url=base_url+ str(page_number)
        response=requests.get(url, headers={"Accept":"text/html"})
        parsed_response=BeautifulSoup(response.text, "html.parser")

        titles=parsed_response.find_all("a", {"itemprop":"url", "class":"results"})
        for title in titles:
             print(title.text)
        sleep(1)
        print("page: ", page_number)
  
        
parse_multiple_urls()