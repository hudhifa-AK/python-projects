with open("ap_docs.txt", "r") as doc_file:
    articles = doc_file.read().replace("\n", " ").replace("  "," ")
articles = articles.split("<NEW DOCUMENT>")
articles = articles[1:]
print(type(articles))
print(articles)