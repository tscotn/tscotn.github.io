import requests
from bs4 import BeautifulSoup
import sys
import os
import cgi

def GetHTML(article_url):
    article_raw = requests.get(article_url)
    article_soup = BeautifulSoup(article_raw.content, 'html.parser')
    return article_soup

def GetRecipeText(article_soup):
#    article_text: str = ''
    for paragraph in article_soup.find_all('ol'):
        return paragraph
        
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
 

InsertTxt(GetArticle(sys.argv[1]))
os.system('open //Users/scot/Desktop/Github/Recipe\ Reader/article.html')

main():
    

if __name__ = '__main__':
    main()
