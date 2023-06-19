import wikipediaapi

def read_titles():
    with open('small.txt', 'r') as file:
        for line in file:
            yield line.strip()

def get_article(title):
    wiki_wiki = wikipediaapi.Wikipedia('pl')
    page = wiki_wiki.page(title)
    if page.exists():
        return page.text
    else:
        return None

def calculate_average_letter_count():
    total_letters = 0
    total_articles = 0

    for title in read_titles():
        article = get_article(title)
        if article:
            total_letters += len(article)
            total_articles += 1

    if total_articles > 0:
        average_letter_count = total_letters / total_articles
        return average_letter_count
    else:
        return 0

average_count = calculate_average_letter_count()
print(f"Średnia liczba liter na artykuł: {average_count}")
