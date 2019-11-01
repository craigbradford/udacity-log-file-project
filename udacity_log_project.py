#!/usr/bin/env python
import psycopg2

# Connect to the news database
conn = psycopg2.connect(dbname="news")

# Open a cursor to perform database operations
cur = conn.cursor()


# create a function that gets the top 3 articles

def top3_articles():
    """
    Return the top three most viewed articles with their view counts.

    Returns:
    A list of two element tuples. Each tuple contains:
      - the title of the article.
      - the number of views for the article

    The list is sorted by number of views in descending order. Only the three
    most viewed articles are returned.
    """

    cur.execute("""
        SELECT title, COUNT(*) AS article_title
        FROM article_summary
        GROUP BY title
        ORDER BY article_title DESC
        LIMIT 3;
    """)
    result = cur.fetchall()
    return result


def top_authors():
    """
    Returns a list of the top authors by article pageviews.

    Returns:
    A list of two element tuplies. Each containins:
        - the author name
        - the total number of sessions all of their articles attracted
    """

    cur.execute("""
        SELECT author, count(*) AS article_author
        FROM article_summary
        GROUP BY author
        ORDER BY article_author DESC;
    """)
    result = cur.fetchall()
    return result


def high_errors():
    """
    Returns a list of dates and the percentage of requests
    that were errors that day

    Returns a list of two element tuples. Each contains:
        - the date
        - the percetange of requests that were not a 200 OK response
    """

    cur.execute("SELECT newdate, percentage FROM stats WHERE percentage > 1;")
    result = cur.fetchall()
    return result


# Call the top articles function
top3_articles = top3_articles()


print("The most popular articles are: \n")
for article in top3_articles:
    print("{0} - {1} views".format(article[0], article[1]))
print("\n")

# Call the top authors function


top_authors = top_authors()


print("The most popular authors are: \n")
for author in top_authors:
    print("{0} - {1} views".format(author[0], author[1]))
print("\n")

# Call the high errors function


high_errors = high_errors()


print("The following days had a high number of errors: \n")
for date in high_errors:
    print("{0} - {1} Error Percentage"
          .format(high_errors[0][0], high_errors[0][1]))
print("\n")
