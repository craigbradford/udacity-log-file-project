# Udacity Log Analysis Project

## Requirements
1. Python3
2. PostgreSQL
3. Vagrant
4. Virtual Box

### How to use
1. Set up Virtual Box and Vagrant
2. [Download the date here](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip)
3. cd into the vagrant folder
4. run ```vagrant up```
5. Connect to the VM using ```vagrant ssh```
6. Run ```psql```
7. Connect to the news database using ```\c news```
8. Create both of the views using the commands in the views section below
9. Run the python script ```python3 udacity_log_project.py```

## Create the following views

**Article Summary View**
```
create view article_summary as
select title, name as author, path1 as path, pageviews
from(
(select authors.name, articles.title, articles.slug, log.path as path1
from authors,articles,log
where authors.id=articles.author
and log.path::text LIKE '%'||articles.slug::text) titles
join
(select log.path as path2, count(*) as pageviews
from log
group by log.path
order by pageviews desc) requestcount
on path1 = path2);
```

**Stats View**

```
create view stats as
select AllRequests.newdate, AllRequests.numrequests, Errors.numerrors,
ROUND(numerrors * 100.0 / numrequests, 1) AS percentage
from (
(select cast(time as date) as newdate, count(*) as numrequests from log
group by newdate
order by numrequests desc) as AllRequests
join
(select cast(time as date) as newdate2, count(*) as numerrors from log
where status != '200 OK'
group by newdate2
order by numerrors desc) Errors
on newdate = newdate2);
```
