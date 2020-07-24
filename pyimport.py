#import pymysql
#import mysql.connector

#import pgdb
#import xml.etree.ElementTree as ET
#import xmltodict
#import pg
#import scrapy
#import lxml
#from lxml import etree

import psycopg2
import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

#creation of engine
engine = create_engine('postgresql+psycopg2://db_user:db_password@host/dd_name')

"""
from sqlalchemy import inspect
inspector = inspect(engine)

for table_name in inspector.get_table_names():
    print(table_name)

    for column in inspector.get_columns(table_name):
       print("Column: %s" % column['name'])
"""

#creation of session
db = scoped_session(sessionmaker(bind=engine))

import glob
filenames = sorted(glob.glob('/Users/CASLoaner/Downloads/pmc-00/**/*.nxml', recursive=True))


import bs4
from bs4 import BeautifulSoup
from datetime import datetime

count = 0
for filename in filenames:
    with open(filename) as file:
        soup = bs4.BeautifulSoup(file, "html.parser")

        user_id = 1
        created_at = datetime.now()

        _title = soup.find("article-title")
        if (_title is not None):
            title = soup.find("article-title").get_text().strip()
        else:
            title = "Title is Empty"

        _journal_id = soup.find("journal-id")
        if (_journal_id is not None):
            journal_id = soup.find("journal-id").get_text().strip()
        else:
            journal_id = 0

        _journal_title = soup.find("journal-title")
        if (_journal_title is not None):
            journal_title = soup.find("journal-title").get_text().strip()
        else:
            journal_title = "Journal Title is Empty"

        _issn_ppub = soup.find("issn", {'pub-type': 'ppub'})
        if(_issn_ppub is not None):
            issn_ppub = soup.find("issn", {'pub-type': 'ppub'}).get_text().strip()
        else:
            issn_ppub = 0

        _issn_epub = soup.find("issn", {'pub-type': 'epub'})
        if(_issn_epub is not None):
            issn_epub = soup.find("issn", {'pub-type': 'epub'}).get_text().strip()
        else:
            issn_epub = 0

        _publisher_name = soup.find("publisher-name")
        if(_publisher_name is not None):
            publisher_name = soup.find("publisher-name").get_text().strip()
        else:
            publisher_name = "Publisher Name is Empty"

        _publisher_loc = soup.find("publisher-loc")
        if(_publisher_loc is not None):
            publisher_loc = soup.find("publisher-loc").get_text().strip()
        else:
            publisher_loc = "Publisher LOC is Empty"

        _article_id_pmid = soup.find("article-id", {'pub-id-type': 'pmid'})
        if (_article_id_pmid is not None):
            article_id_pmid = soup.find("article-id", {'pub-id-type': 'pmid'}).get_text().strip()
        else:
            article_id_pmid = "Article ID PMID is Empty"

        _article_id_pmc = soup.find("article-id", {'pub-id-type': 'pmc'})
        if (_article_id_pmc is not None):
            article_id_pmc = soup.find("article-id", {'pub-id-type': 'pmc'}).get_text().strip()
        else:
            article_id_pmc = "Article ID PMC is Empty"

        _article_id_publisher_id = soup.find("article-id", {'pub-id-type': 'publisher-id'})
        if (_article_id_publisher_id is not None):
            article_id_publisher_id = soup.find("article-id", {'pub-id-type': 'publisher-id'}).get_text().strip()
        else:
            article_id_publisher_id = "Publisher ID is Empty"

        _article_id_doi = soup.find("article-id", {'pub-id-type': 'doi'})
        if (_article_id_doi is not None):
            article_id_doi = soup.find("article-id", {'pub-id-type': 'doi'}).get_text().strip()
        else:
            article_id_doi = "Article ID DOI is Empty"

        _article_subject = soup.find("subject")
        if (_article_subject is not None):
            article_subject = soup.find("subject").get_text().strip()
        else:
            article_subject = "Article Subject is Empty"

        _article_title = soup.find("article-title")
        if (_article_title is not None):
            article_title = soup.find("article-title").prettify(formatter="html")
        else:
            article_title = "Article Title is Empty"

        _contrib_group = soup.find("contrib-group")
        if (_contrib_group is not None):
            contrib_group = soup.find("contrib-group").prettify(formatter="html")
        else:
            contrib_group = "Contributors are Empty"

        _aff1 = soup.find("aff", {'id': 'I1'})
        if (_aff1 is not None):
            aff1 = soup.find("aff", {'id': 'I1'}).prettify(formatter="html")
        else:
            aff1 = "Aff is Empty"

        _aff2 = soup.find("aff", {'id': 'I2'})
        if (_aff2 is not None):
            aff2 = soup.find("aff", {'id': 'I2'}).prettify(formatter="html")
        else:
            aff2 = " "

        _aff3 = soup.find("aff", {'id': 'I3'})
        if (_aff3 is not None):
            aff3 = soup.find("aff", {'id': 'I3'}).prettify(formatter="html")
        else:
            aff3 = " "

        _pub_date_ppub = soup.find("pub-date", {'pub-type': 'ppub'})
        if (_pub_date_ppub is not None):
            pub_date_ppub = soup.find("pub-date", {'pub-type': 'ppub'}).prettify(formatter="html")
        else:
            pub_date_ppub = 0

        _pub_date_epub = soup.find("pub-date", {'pub-type': 'epub'})
        if (_pub_date_epub is not None):
            pub_date_epub = soup.find("pub-date", {'pub-type': 'epub'}).prettify(formatter="html")
        else:
            pub_date_epub = 0

        _volume = soup.find("volume")
        if (_volume is not None):
            volume = soup.find("volume").get_text().strip()
        else:
            volume = 0

        _issue = soup.find("issue")
        if (_issue is not None):
            issue = soup.find("issue").get_text().strip()
        else:
            issue = 0

        _fpage = soup.find("fpage")
        if (_fpage is not None):
            fpage = soup.find("fpage").get_text().strip()
        else:
            fpage = 0

        _lpage = soup.find("lpage")
        if (_lpage is not None):
            lpage = soup.find("lpage").get_text().strip()
        else:
            lpage = 0

        _history = soup.find("history")
        if (_history is not None):
            history = soup.find("history").prettify(formatter="html")
        else:
            history = 0

        _copyright_statement = soup.find("copyright-statement")
        if (_copyright_statement is not None):
            copyright_statement = soup.find("copyright-statement").get_text().strip()
        else:
            copyright_statement = "Copyright Statement is Empty"

        _abstract = soup.find("abstract")
        if (_abstract is not None):
            abstract = soup.find("abstract").prettify(formatter="html")
        else:
            abstract = "Abstract is Empty"

        _keywords = soup.find("kwd-group")
        if (_keywords is not None):
            keywords = soup.find("kwd-group").prettify(formatter="html")
        else:
            keywords = "Keywords are Empty"

        _body = soup.find("body")
        if (_body is not None):
            body = soup.find("body").prettify(formatter="html")
        else:
            body = "Body is Empty"

        _sec_methods = soup.find("sec", {'sec-type': 'methods'})
        if (_sec_methods is not None):
            sec_methods = soup.find("sec", {'sec-type': 'methods'}).prettify(formatter="html")
        else:
            sec_methods = "Section Methods is Empty"

        _sec_display_objects = soup.find("sec", {'sec-type': 'display-objects'})
        if (_sec_display_objects is not None):
            sec_display_objects = soup.find("sec", {'sec-type': 'display-objects'}).prettify(formatter="html")
        else:
            sec_display_objects = "Display Objects are Empty"

        _ref_list = soup.find("ref-list")
        if(_ref_list is not None):
            ref_list = soup.find("ref-list").prettify(formatter="html")
        else:
            ref_list = "Reference List are Empty"

        db.execute("INSERT INTO articles_articles (title,user_id,created_at,journal_id,journal_title,issn_ppub,issn_epub,publisher_name,publisher_loc,article_id_pmid,article_id_pmc,article_id_publisher_id,article_id_doi,article_subject,article_title,contrib_group,aff1,aff2,aff3,pub_date_ppub,pub_date_epub,volume,issue,fpage,lpage,history,copyright_statement,abstract,keywords,body,sec_methods,sec_display_objects,ref_list) VALUES (:title,:user_id,:created_at,:journal_id,:journal_title,:issn_ppub,:issn_epub,:publisher_name,:publisher_loc,:article_id_pmid,:article_id_pmc,:article_id_publisher_id,:article_id_doi,:article_subject,:article_title,:contrib_group,:aff1,:aff2,:aff3,:pub_date_ppub,:pub_date_epub,:volume,:issue,:fpage,:lpage,:history,:copyright_statement,:abstract,:keywords,:body,:sec_methods,:sec_display_objects,:ref_list)", {"title":title, "user_id":user_id, "created_at":created_at, "journal_id":journal_id, "journal_title":journal_title, "issn_ppub":issn_ppub, "issn_epub":issn_epub, "publisher_name":publisher_name, "publisher_loc":publisher_loc, "article_id_pmid":article_id_pmid, "article_id_pmc":article_id_pmc, "article_id_publisher_id":article_id_publisher_id, "article_id_doi":article_id_doi, "article_subject":article_subject, "article_title":article_title, "contrib_group":contrib_group, "aff1":aff1, "aff2":aff2, "aff3":aff3, "pub_date_ppub":pub_date_ppub, "pub_date_epub":pub_date_epub, "volume":volume, "issue":issue, "fpage":fpage, "lpage":lpage, "history":history, "copyright_statement":copyright_statement, "abstract":abstract, "keywords":keywords, "body":body, "sec_methods":sec_methods, "sec_display_objects":sec_display_objects, "ref_list":ref_list})
        count = count + 1
        print(filename,count,created_at)

    # commit the changes
    db.commit()

    # close the session
    db.close()

print("Mission is Complete!")

