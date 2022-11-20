from urllib.request import urlopen
from bs4 import BeautifulSoup

###########################################################

web_page = urlopen('https://www.finn.no/job/fulltime/search.html?sort=RELEVANCE')

###########################################################


# Getting all the links from the first page and adding them in a list()
def get_links() -> list:
    internal_links = []

    bs = BeautifulSoup(web_page, 'html.parser')

    for links in bs.find_all('a', {'class': 'ads__unit__link'}):  # All links I want are related to this class
        internal_links.append(links.attrs['href'])  # Adding only the link

    return internal_links
# _________________________________________________________


# Getting the title and the first paragraph of all links I've found
def get_title_and_paragraph():
    data = {}  # I could put in a dict() but it'll demand much more memory and processing

    for link in get_links():  # Accessing the links from the obtained list

        if link.startswith('/'):  # The first link do not have the full domain - fixing it
            link = f'https://www.finn.no{link}'

        new_site = urlopen(link)
        bs = BeautifulSoup(new_site, 'html.parser')

        # Uncomment only if it is needed store in the dict()
        """data[bs.find('h1', {'class': 'u-t2'}).get_text()] = bs.find('p')"""

        print(f"{bs.find('h1', {'class': 'u-t2'}).get_text()}"  # Showing the Title
              f"\n\t-| {bs.find('p').get_text()}\n\n")  # Showing the first paragraph

###########################################################


get_title_and_paragraph()
