html_doc="""
<html>
 <head>
 <title>
 The Dormouse's story
 </title>
 </head>
 <body>
  <p class="title">
   <b>
   The Dormouse's story
 </b>
  </p>
  <p class="story">
   Once upon a time there were three little sisters; and their names were
   <a class="sister" href="http://example.com/elsie" id="link1">
    Elsie
   </a>
   ,
   <a class="sister" href="http://example.com/lacie" id="link2">
    Lacie
               </a>
   and
   <a class="sister" href="http://example.com/tillie" id="link2">
    Tillie
   </a>
   <a class="sister" href="http://example1.com/elsie" id="link1">Elsie</a>,
   <a class="sister" href="http://example2.com/lacie" id="link2">Lacie</a>,
   <a class="sister" href="http://example3.com/tillie" id="link3">Tillie</a>]
   ; and they lived at the bottom of a well.
 </p>
  <p class="story">
   ...
  </p>
 </body>
</html>
"""
from bs4 import BeautifulSoup

soup = BeautifulSoup(html_doc, 'html.parser')


result=soup.prettify()# html dosyasını düzenler.
#print(result)
# result=soup.title
# print(result)
# result=soup.title.name
# print(result)
# result=soup.title.string
# print(result)
# result=soup.body
# print(result)
# result=soup.head
# print(result)
# result=soup.find_all("p")[1].find_all("a")
# print(result)

# result=soup.findChildren("head")
# print(result)
# result=soup.p.findNextSibling().findNextSibling()
# print(result)result=soup.p.findNextSibling().findNextSibling()
# print(result)
result=soup.find_all("a")[0]
print(result.get("href"))
# for link in result:
#     print((link.get("href"))[:10])

