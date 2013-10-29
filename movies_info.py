import re 
from bs4 import BeautifulSoup
from zip_code import create_soup

def main(url = "http://www.imdb.com/showtimes/cinema/US/ci0002452/US/08904"):
    
    soup = create_soup(url)
    
    movie_info = movie_html(soup)
    
    movie_info = scrape_info(movie_info)
    

def scrape_info(html):
    """
    Will scrape the movie data that I want.
    """
    for item in html:
        item = str(item)
        
        movie_name(item)
        movie_poster(item)
        movie_duration(item)
        movie_categories(item)
        movie_showtimes(item)
    """
    find_title = re.compile('itemprop="url">(.*)</a>')
    theater_title = re.findall(find_title, str(theater_html1))
    """

def movie_showtimes(html):
    """
    Scrapes movie showtimes for regular, 3D and Imax
    """
    
    soup = BeautifulSoup(html)
    soup = soup.find_all("div", {"class": "showtimes"})
    
    print "\n"
    
    for stuff in soup:
        #print stuff
        
        times = re.compile('data-displaytimes="(.*)" data-logo-url')
        times = re.findall(times, str(stuff))
        
        #print times

def movie_categories(html):
    """
    Scrapes movie categories
    """
    
    """
    categories = re.compile('time>(.*)')
    categories = re.findall(categories, html)
    
    print categories
    """
    
    soup = BeautifulSoup(html)
    soup = soup.find("p", {"class":"cert-runtime-genre"})
    
    #print soup
    #print soup.strings
    
    for string in soup.strings:
        
        string = str(string).split("\n")
        #print "\n\n"
        
        for item in string:
            try:
                if item[0].isalpha():
                    #print item
                    pass
            except:
                pass
            
def movie_duration(html):
    """
    Scrapes movie duration (if it exists)
    """

    duration = re.compile('duration">(.*)<')
    duration = re.findall(duration, html)
    
    #print duration

def movie_poster(html):
    """
    Scrapes movie poster url and rating url (if it exists)
    """
    poster = re.compile('src="(.*)" title')
    poster = re.findall(poster, html)
    
    #print poster
        

def movie_name(html):
    """
    Scrapes movie titel
    """
    name = re.compile('alt="(.*)" height')
    name = re.findall(name, html)
    name = name[0][:-6]
    
    #print "name:", name, "\n"
    
    


    
def movie_html(soup):
    
    even = soup.find_all("div", {"class": "list_item even"})
    
    odd  = soup.find_all("div", {"class": "list_item odd"})
    
    #print even[0], "\n", odd[0], "\n\n", type(even), "\n", len(even)
    
    stack = even + odd
    
    return stack
    
if __name__ == "__main__":
    main()
