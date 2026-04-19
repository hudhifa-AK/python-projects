import string

def extract_articles() -> list:
    with open("ap_docs.txt", "r") as doc_file:
        articles = doc_file.read()
    articles = articles.split("<NEW DOCUMENT>")
    articles = articles[1:]
    return articles

def populate_word_index(article_list: list) -> dict:
    word_index = {}
    for doc_id, article in enumerate(article_list, start=1):

        words = article.split()
        word_list = [word.lower().strip().strip(string.punctuation) for word in words]

        for word in word_list:
            if word in word_index:
                word_index[word].add(doc_id)
            else:
                word_index[word] = {doc_id}
    return word_index

def search_word_index(search_input: str, word_index: dict) -> set:
    search_words = [search.lower().strip().strip(string.punctuation) for search in search_input.split()]

    search_list = [word_index[word] for word in search_words if word in word_index]

    search_results = search_list[0].copy()
    for s in search_list[1:]:
        search_results &= s
    return search_results

while True:
    print("What would you like to do?\n 1. Search for documents\n 2. Read Document\n 3. Quit Program")
    try:
        choice = int(input())

        if choice == 1:
            user_search_words = str(input("Enter search words: "))
            search_options = search_word_index(user_search_words, populate_word_index(extract_articles()))
            print("Documents fitting search:")
            print(' '.join(str(option) for option in search_options))

        elif choice == 2:
            user_search_article = int(input("Enter document number: "))
            user_search_article -= 1
            picked_doc = extract_articles()
            print(picked_doc[user_search_article])
        elif choice == 3:
            break
        else:
            print("Invalid choice. Please try again with 1, 2 or 3.")

    except ValueError:
        print("Error: Please enter a valid choice\n")
        continue

    except IndexError:
        print("Error: Please enter a valid choice\n")
        continue

