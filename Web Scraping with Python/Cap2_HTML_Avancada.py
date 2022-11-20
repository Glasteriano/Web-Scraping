from bs4 import BeautifulSoup
from urllib.request import urlopen


site = urlopen('https://www.pythonscraping.com/pages/warandpeace.html')
bs = BeautifulSoup(site.read(), 'html.parser')


name_list = bs.find_all('span', {'class': 'green'})  # Preciso do nome da Tag e do Atributo dessa Tag como parâmetro
lista_nome = []
for name in name_list:
    print(f'\n- Nome cru: {name}\n'  # Mostra o conteúdo junto com a Tag
          f'\t-- Nome sem Tag: {name.get_text()}\n')  # Mostra apenas o texto na Tag

########################################################################################################################

# Mostrando a diferença de usar a função .children da função .descendants
# .children não vai tão profundo quanto .descendants

site2 = urlopen('https://pythonscraping.com/pages/page3.html')
bs = BeautifulSoup(site2, 'html.parser')

for child in bs.find('table', {'id': 'giftList'}).children:
    print(child)

for child in bs.find('table', {'id': 'giftList'}).descendants:
    print(child)

########################################################################################################################


# Usando a função .next_siblings
# Usando bastante em tabelas com títulos para não colotar também o título da tabela

site3 = urlopen('https://pythonscraping.com/pages/page3.html')
bs = BeautifulSoup(site3.read(), 'html.parser')

for sibling in bs.find('table', {'id': 'giftList'}).tr.next_siblings:
    print(sibling)
    print(sibling.get_text())

########################################################################################################################

# Usando a função .parent/.parents para achar o pai da Tag e com isso achar seus irmãos predecessores

site4 = urlopen('https://pythonscraping.com/pages/page3.html')
bs = BeautifulSoup(site4.read(), 'html.parser')

previous_one = bs.find('img', {'src': '../img/gifts/img1.jpg'}).parent.previous_sibling.get_text()

print(previous_one)
