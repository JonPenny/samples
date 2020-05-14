from newspaper import Article

url = 'https://wheniwork.com/blog/12-ways-you-can-use-your-when-i-work-account-to-navigate-covid-19'
article = Article(url)
article.download()
article.parse()

def find_author(newspaper_article):
    # See if newspaper finds the articles authors
    if article.authors and len(article) != 0:
        return article.authors
    # If not attempt our own method
    else:
        search_term = "author"
        loc = 0

        # Step through all of the html picking out all of the classes
        while loc != -1:
            new_loc = article.html[loc:].find("class=")
            if new_loc == -1:
                break

            # Check if the class has the search term we want in it.
            if article.html[loc:loc+70].find(search_term) != -1:

                # Remove the surrounding div
                div_start = article.html[loc:loc+70].find(">") + 1
                div_end = article.html[loc:loc+70].find("</div>")

                author_html_text = (article.html[loc+div_start:loc+div_end])

                # Remove any extra html elements
                # I would improve this part as part of the project, elements should be removed by
                # element, not simply removing the span encapsulation
                author = author_html_text.replace("<span>","").replace("</span>","")
                return author

            # Update our original search index
            loc += new_loc + 1

print(find_author(article))

