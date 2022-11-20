from urllib.request import urlopen
from bs4 import BeautifulSoup


links = []

site = urlopen('https://www.finn.no/job/fulltime/search.html?sort=RELEVANCE')
bs = BeautifulSoup(site, 'html.parser')
# ___________________________________________________________________________________________

# Aqui analiso a Tag h2 para pegar a Tag de link - porém alguns h2 não tem Tag de link e pode ocorrer êrro

for main_tag in bs.find_all('h2'):  # Analisando na Tag principal onde ficam os links
    for link in main_tag.find_all('a'):  # Procurando a Tag de link 'a' dentro de 'h2'
        # print(link.attrs['href'])  # Apenas conferindo se são os links certos
        links.append(link.attrs['href'])  # Adicionando na lista
# ___________________________________________________________________________________________

# Aqui analiso directamente a classe onde os links estão associados
# evito de pegar Tags indesejadas e possíveis êrros

for all_in in bs.find_all('a', {'class': 'ads__unit__link'}):
    print(all_in.attrs['href'])


""" Uncomment only if you really want to check the list link """
# for list_link in links:
#     print(list_link)
