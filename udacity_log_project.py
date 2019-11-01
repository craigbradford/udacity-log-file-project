#!/usr/bin/env python
import psycopg2

# Connect to the news database
conn = psycopg2.connect(dbname="news")

# Open a cursor to perform database operations
cur = conn.cursor()


# create a function that gets the top 3 articles

def top3_articles():

    # Query the database and obtain data as Python objects

    cur.execute("select title, count(*) as article_title from "
                "article_summary group by title order "
                "by article_title desc limit 3;")
    result = cur.fetchall()
    return result


# create a function that gets the top authors

def top_authors():

    # Query the database and obtain data as Python objects
    cur.execute("select author, count(*) as article_author from "
                "article_summary group by author order "
                "by article_author desc;")
    result = cur.fetchall()
    return result


# create a function that finds days with a high number of errors

def high_errors():

    # Query the database and obtain data as Python objects
    cur.execute("select newdate, percentage from stats where percentage > 1;")
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
