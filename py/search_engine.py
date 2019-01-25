from datetime import datetime

from elasticsearch_dsl import Index, Document, Date, Integer, Keyword, Text, Ip, analyzer
import elasticsearch_dsl as es
from elasticsearch_dsl.connections import connections

connections.create_connection(hosts=['localhost'])
INDEX_NAME="crepuscule"

PAGE_BREAK = "\u000c"

class Paragraph(Document):
    page = Integer()
    section = Integer()
    text = Text(analyzer=analyzer('french'))

    class Index:
        name = INDEX_NAME



def index(path):
    par_idx = 0
    sec_idx = 1
    page = 1
    with open(path) as f:
        for line in f:
            par_idx += 1
            if line.startswith("*"):
                sec_idx += 1
                txt = line[1:].strip()
            else:
                txt = line.strip()
            page += txt.count(PAGE_BREAK)
            p = Paragraph(page = page,
                          section = sec_idx,
                          text = txt)
            p.save()


def query(q):
    s = Paragraph.search().query("match", text=q)
    r = s.execute()
    for p in r:
        yield p


