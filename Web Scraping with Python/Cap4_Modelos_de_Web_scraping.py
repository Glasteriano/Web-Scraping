from urllib.request import urlopen
from bs4 import BeautifulSoup
from datetime import datetime

#########################################################################################

target = 'https://www.finn.no/job/fulltime/search.html?sort=RELEVANCE'

#########################################################################################


def access_site(target_site) -> BeautifulSoup:  # Setting the Soup once to call it when the parse is needed
    site = urlopen(target_site)

    return BeautifulSoup(site, 'html.parser')
# _______________________________________________________________________________________


def get_links() -> list:  # Function that get all links found on the page and store them
    internal_links = []
    links_found = 0

    bs = access_site(target)

    for link in bs.find_all('a', {'class': 'ads__unit__link'}):
        internal_links.append(link.attrs['href'])
        links_found += 1

    # Just for visualisation purpose to know how many links were stored
    print(f'{links_found} links adicinados!' if links_found != 1 else
          '1 link adicionado!')

    return internal_links
# _______________________________________________________________________________________


def normalise_link(link) -> str:  # Some links don't have the full address
    if link.startswith('/'):
        link = f'https://www.finn.no{link}'  # Solving that incomplete link problem

    return link
# _______________________________________________________________________________________


def get_title(link) -> str:
    return access_site(normalise_link(link)).find('h1', {'class': 'u-t2'}).get_text()
# _______________________________________________________________________________________


def get_location(link) -> str:  # Some links don't have the location
    try:
        return access_site(normalise_link(link)).find('a', {'data-controller': 'trackCrumbTrailAttribute3'}). \
            get_text()

    except AttributeError:
        return 'Unknown Location'
# _______________________________________________________________________________________


def show_result() -> None:
    result = {}  # Store the location as key and the title as value
    add = 0

    for link in get_links():

        if get_location(link) not in result.keys():  # Checking the nonexistence of the locatiion in dict()
            result[get_location(link)] = [get_title(link)]
        else:
            result[get_location(link)].append(get_title(link))

        add += 1

        # Also for visualisation purpose to know if all links found were added
        print(f'{add} links analisados' if add != 1 else '1 link analisado')

    for key, value in sorted(result.items()):  # Showing the dict() in undestandable layout
        print()
        print(key)

        for list_item in value:
            print(f'\t-| {list_item}')

        print(f'\n\t\t-> Total job openings: {len(result[key])}')
        print()
# _______________________________________________________________________________________


a = datetime.now()

show_result()

b = datetime.now()

print(b-a)  # Getting the total time it takes to run and complete the task
