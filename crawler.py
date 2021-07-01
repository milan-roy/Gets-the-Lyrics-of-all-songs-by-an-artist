import requests
import bs4

from sys import argv
def parser(content):
    return bs4.BeautifulSoup(content,features="html.parser")

def crawler(url):
    get_back=requests.get(url)
    return parser(get_back.content)

def get_lyrics(url):
    page_content=crawler(url)
    content=page_content.find_all("pre",class_="lyric-body")    
    content2=parser(str(content))
    return content2.text    


def main():
    links=[]
    names=[]
    names_links={}

    url=argv[1]
    page_content=(crawler(url))    
    
    for i in page_content.find_all("td", class_="tal qx"):
        links.append(i.find('a')['href'])
        name_temp=i.text
        if '\\' in name_temp:
            list1= name_temp.split('\\')
            name_temp=''.join(list1)

        if '/' in name_temp:
            list1= name_temp.split('/')
            name_temp=''.join(list1)

        names.append(name_temp)

    for i in range (len(links)):
        names_links[names[i]]=links[i]
    
    for key, val in names_links.items():
        lyrics=get_lyrics("https://www.lyrics.com"+str(val))
        file1=open(str(key)+".txt",'w')
        file1.write(lyrics)
        file1.close()
       

    return 0


main()