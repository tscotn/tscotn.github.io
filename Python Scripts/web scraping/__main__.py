#!/usr/bin/env python

import requests
from bs4 import BeautifulSoup
import sys
import os

def GetHTML(article_url):
    article_raw = requests.get(article_url)
    article_soup = BeautifulSoup(article_raw.content, 'html.parser')
    return article_soup


#def GetArticleHeader(article_soup):
#    article_header: str = ''
#    for header in article_soup.find_all('h3'):
#        article_header += header.get_text()
#    return article_header


def GetRecipeText(article_soup):
#    article_text: str = ''
    for paragraph in article_soup.find_all('p'):
        return paragraph
#        article_text += paragraph.get_text()
#    return article_text


def GetArticle(article_url):
    article_soup = GetHTML(article_url)
#    article = GetArticleHeader(article_soup) + "\n" + GetArticleText(article_soup)
    article = GetRecipeText(article_soup)
    return article#[:article.find("Comment")]


def InsertTxt(article):  # this opens/creates a new .txt file, writes webText to it, closes .txt file
    file = "//Users/scot/Desktop/Github/Recipe Reader/article.html"
    f = open(file, "w+")
    f.write('<!DOCTYPE html><html><body>' + str(article) + '</body></html>')
    f.close()

#url = requests.GET("url")
#print(url)

InsertTxt(GetArticle(sys.argv[1]))
os.system('open //Users/scot/Desktop/Github/Recipe\ Reader/article.html')

# take a link as a sysargv, return article text, launch html file that formats the article in browser, save link in file?

