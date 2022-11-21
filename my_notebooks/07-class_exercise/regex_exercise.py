import bs4, re, requests

# Using regex find out how many times ‘Turing’ is used in the article
url = "https://en.wikipedia.org/wiki/Alan_Turing"
r = requests.get(url)
r.raise_for_status()
soup = bs4.BeautifulSoup(r.text, "html.parser")

turings = re.compile(r'Turing')

output = turings.findall(soup.text)


print(f"Amount of times Turing appeared in text: {len(output)}")

# Find all the sentences that has a year in them
# (sentence defined by: starting at \n or dot or comma and ending at dot or comma.
# Gets every year in every sentence:
#sentence_with_year = re.compile(r'.*([1-3][0-9]{3})')

# Gets the word before the year:
#sentence_with_year = re.compile(r'^\n|. (\w+).+(\d{4})')

# Tsukani's solution:
sentence_with_year = re.compile(r'[^.,\n]*\d{4,4}[$.,\n]')


year_output = sentence_with_year.findall(soup.text)
for sentence in year_output:
    print(sentence)
