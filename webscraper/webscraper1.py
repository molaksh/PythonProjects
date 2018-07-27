import bs4
from urllib2 import urlopen as uReq
from bs4 import BeautifulSoup as soup

filename = "100 books to read in a lifetime.csv"
f = open(filename, "w")
header = "title|author|link\n"
f.write(header)


my_url = 'https://www.amazon.com/b/ref=bhp_brws_100bks?ie=UTF8&node=8192263011&pf_rd_m=ATVPDKIKX0DER&pf_rd_s=merchandised-search-leftnav&pf_rd_r=WJSJEX5BAM0005XFQS3S&pf_rd_r=WJSJEX5BAM0005XFQS3S&pf_rd_t=101&pf_rd_p=742c6a94-145d-4c8a-aeb5-5dd9096fb8b6&pf_rd_p=742c6a94-145d-4c8a-aeb5-5dd9096fb8b6&pf_rd_i=283155'

uClient = uReq(my_url)
pg_html = uClient.read()
uClient.close()

#full page
page_soup = soup(pg_html, "html.parser")

#code not working from here as the page html tags are changed

#the items needed from the webpage
containers = page_soup.findAll("li",{"class":"acswidget-carousel-redesign__card"})

for container in containers:
    names = container.findAll("span",{"class":"a-truncate-full"})
    #containers_for_link = container.findAll("a",{"class":"a-link-normal"})
    
    for name in names:
        book_title = names[0].text
        author_name = names[1].text

    # for container_for_link in containers_for_link:
    #     link = containers_for_link[container_for_link]
    #     x=1+1

    for a in container.findAll("a", href=True):
        #print("link: ", a['href'])
        link = a['href']
        break

    


    print("book title: " + book_title)
    print("author: " + author_name)
    print("link: " + link)
    
    f.write(book_title.replace(","," ") + "|" + author_name + "|" +"http://www.amazon.com"+link + "\n")
    
f.close()