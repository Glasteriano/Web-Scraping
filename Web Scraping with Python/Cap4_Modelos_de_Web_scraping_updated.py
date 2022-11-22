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
    bs = access_site(target)

    internal_links = [link.attrs['href'] for link in bs.find_all('a', {'class': 'ads__unit__link'})]

    # Just for visualisation purpose to know how many links were stored
    print(f'{len(internal_links)} links adicinados!' if len(internal_links) != 1 else
          '1 link adicionado!')

    return internal_links
# _______________________________________________________________________________________


def normalise_link(link) -> str:  # Some links don't have the full address
    return f'https://www.finn.no{link}' if link.startswith('/') else link  # Solving that incomplete link problem
# _______________________________________________________________________________________


def get_title(link) -> str:
    return access_site(normalise_link(link)).find('h1', {'class': 'u-t2'}).get_text()
# _______________________________________________________________________________________


def get_location(link) -> str:  # Some links don't have the location
    try:
        return access_site(normalise_link(link))\
            .find('a', {'data-controller': 'trackCrumbTrailAttribute3'}).get_text()

    except AttributeError:
        return 'Unknown Location'
# _______________________________________________________________________________________


def show_result() -> None:
    result = {}  # Store the location as key and the title as value
    add = 0

    for link in get_links():

        if get_location(link) not in result.keys():  # Checking the nonexistence of the location in dict()
            result[get_location(link)] = [get_title(link)]
        else:
            result[get_location(link)].append(get_title(link))

        add += 1

        # Also for visualisation purpose to know if all links found were added
        print(f'{add} links analisados' if add != 1 else '1 link analisado')

    for key, value in sorted(result.items()):  # Showing the dict() in undestandable layout
        print(f'\n{key}')

        for list_item in value:
            print(f'\t-| {list_item}')

        print(f'\n\t\t-> Total job openings: {len(result[key])}\n')
# _______________________________________________________________________________________


a = datetime.now()

show_result()

b = datetime.now()

print(b-a)  # Getting the total time it takes to run and complete the task
