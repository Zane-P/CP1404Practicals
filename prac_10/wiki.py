
import wikipedia

search_summary = input("Search for >>> ")
while search_summary != "":
    try:
        wiki_page = wikipedia.page(search_summary)
        print("{}\n{}\n{}\n".format(wiki_page.title, wiki_page.url, wiki_page.summary))
    except wikipedia.exceptions.DisambiguationError as e:
        print(e.options)
    search_summary = input("Search for >>> ")