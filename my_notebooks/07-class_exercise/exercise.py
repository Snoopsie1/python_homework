import bs4
import requests

# Make a request to: https://en.wikipedia.org/wiki/Alan_Turing
url = 'https://en.wikipedia.org/wiki/Alan_Turing'
r = requests.get(url)
r.raise_for_status()
soup = bs4.BeautifulSoup(r.text, 'html.parser')

# and print out the responses .text property
# print(soup)

# Find and print the title of the response page
title = soup.select('title')[0].text
# print(title)

# Find and print content of the first p tag that has content.
# TODO: [JUST FOR FUN ] Try and make a dynamic function,
#  so you don't have to manually input an index
# p_has_content = soup.select('p')[1].text
# print(p_has_content)

# Find and print all content from the TOC
div_id_toc = soup.select('div[class=toc] > ul')
print(div_id_toc)

# Create a dictionary from the TOC links
# like: {‘first link’:’#this_is_the_first_link}
# TODO: Get a list of a href from toc
toc = soup.select('div[class=toc] > ul > li > a')
print(toc)
hrefs = []
for href in toc:
    hrefs.append(url + href.get('href'))

# TODO: Make dict from list
toc_dict = {
    "first link": hrefs[0],
    "second link": hrefs[1],
    "third link": hrefs[2],
    "fourth link": hrefs[3],
    "fifth link": hrefs[4],
    "sixth link": hrefs[5],
    "seventh link": hrefs[6],
}

for key, value in toc_dict.items():
    print(f"{key.title()}: {value}")

# Vincent's Løsning:
outer_toc = soup.select('.toc > ul > li')
inner_toc = soup.select('.toc > ul > li > ul > li')

toc_dict = {}
for el in outer_toc:
    text = el.getText()
    a = el.select('a')
    val = a[0].get('href')
    key = text.split(" ", 1)[1]
    key = key.split("\n")[0]
    toc_dict[key] = val

for el in inner_toc:
    text = el.getText()
    a = el.select('a')
    val = a[0].get('href')
    key = text.split(" ", 1)[1]
    key = key.split("\n")[0]
    toc_dict[key] = val

print(toc_dict)


# Create a function that can take a word and
# look for it in the dictionary keys and
# then return the content from the first link that matches.
# Return the next p elements until next headline (h3 element).

def print_p_tag_from_headline(headline):
    key_found = False
    for key in toc_dict.keys():
        if key != headline:
            print("Looking for key..")
        if key == headline:
            print("Key found!")
            key_found = True

    #if key_found:
        #r = requests.get(url + "#" + word)
        #r.raise_for_status()
        #func_soup = bs4.BeautifulSoup(r.text, "html.parser")
        #h3_tags = func_soup.select('h3')[0].getText()
        #p_tags = func_soup.select('p')[1].getText()

        #return p_tag

    p_content = []

    if key_found:
        r = requests.get(url + "#" + headline)
        r.raise_for_status()
        func_soup = bs4.BeautifulSoup(r.text, "html.parser")
        html_text = func_soup.select('div[id=mw-content-text] > div[class=mw-parser-output]')
        for element in html_text:
            if element.name == 'h3' and element.getText() == headline:
                if element.name == 'p':
                    p_content.append(element.text)
                if element.name == 'h3':
                    break
        return p_content
    else:
        return "No key found! :("

print(print_p_tag_from_headline("Early life and education"))
# TO BE CONTINUED
