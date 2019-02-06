from datetime import datetime

import click
from flask.cli import with_appcontext

from elasticsearch_dsl import Index, Document, Date, Integer, Keyword, Text, analyzer
from elasticsearch_dsl.connections import connections

connections.create_connection(hosts=['localhost'])
INDEX_NAME="crepuscule"
PAGE_BREAK = "\u000c"

from uuid import uuid4
def uuid():
    return uuid4().hex


class Paragraphe(Document):
    
    text = Text(analyzer=analyzer('french'))
    keywords = Keyword(analyzer=analyzer('french'))
    num = Integer()
    page = Integer()
    uid = Keyword()

    @staticmethod
    def simple_search(query, start, limit):
        s = Paragraphe \
            .search() \
            .query("match", text=query)

        r  = [p for p in s.execute()]

        return {"count":len(r), "hits": r}


    class Index:
        name = INDEX_NAME
        
  
def init_app(app):
    
    app.teardown_appcontext(close_app)
    app.cli.add_command(index)
    app.cli.add_command(test_query)


def close_app(app):
    pass
    


@click.command('index')
@click.option('--txt')
@with_appcontext
def index(txt):
    click.echo("deleting index %s" % INDEX_NAME)
    idx = Index(INDEX_NAME)
    idx.delete(ignore=404)
    Paragraphe.init()
    click.echo("Elasticsearch schema initialized")
    click.echo("parsing crepuscule texte")

    if txt is None:
        txt = "./crepuscule.txt"

    secnum = 0
    count = 0
    text = ""
    page = 1
    keywords = []

    with open(txt) as f:
        for line in f.readlines():
            count = count + 1
            if line.strip()[0] == "*":
                secnum += 1
                index_paragraph(text, keywords, page, secnum)
                text = line[1:]
            else:
                text = text + line

            page += line.count(PAGE_BREAK)

    if text != "":
        index_paragraph(secnum + 1, text, keywords)


def index_paragraph(pcount, text, keywords):
    click.echo("+paragraphe : %s %s" % (pcount, len(text)))
    p = Paragraphe(
        text = text,
        keywords = keywords,
        num = pcount,
        uid = uuid()
    )
    p.save()


@click.command('query-es')
@click.option('--query')
@with_appcontext
def test_query(query):
    s = Paragraphe\
        .search()\
        .query("match", text=query)
    for p in s.scan():
        click.echo( "%s :::: %s " % (p.num, p.text))



