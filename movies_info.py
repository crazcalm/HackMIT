import re, scraper1 
from bs4 import BeautifulSoup
from zip_code import create_soup


def main(url = "ci0002452/US/08904"):
        
    url = "http://www.imdb.com/showtimes/cinema/US/"+url

    
    soup = create_soup(url)
    
    movie_info = movie_html(soup)
    
    movie_info = scrape_info(movie_info)
    
    # I need the theater name, again...
    movie_theater = theater_name(soup)
   
    return (movie_theater, movie_info)
    

def scrape_info(html):
    """
    Will scrape the movie data that I want.
    """
    # Will be a list of dicts (movie info)
    all_info = []
    
    for item in html:
        item = str(item)
        
        #print "\n\norigin:\t", item
        
        # Will store the info for individual movies.
        movie_info = {}
        
        
        
        name              = movie_name(item)
        poster_and_rating = movie_poster(item)
        duration          = movie_duration(item)
        categories        = movie_categories(item)
        showtimes         = movie_showtimes(item)
        
        movie_info["name"] = name
        movie_info["poster_and_rating"] = poster_and_rating
        movie_info["duration"] = duration
        movie_info["categories"] = categories
        movie_info["showtimes"] = showtimes
        
        scraper1.download_img(movie_info["poster_and_rating"], movie_info["name"])
        
        movie_info["poster_name"] = str(name)+".jpg"
        movie_info["rating_name"] = str(name)+".png"
        
        all_info.append(movie_info)
        
    for item in all_info:
        print "\n"
        for key in item:
            print key, item[key]
   
    return all_info

def theater_name(html):
    """
    Scrapes the name of the theater
    """
    #soup = BeautifulSoup(html)
    soup = html.find("h1", {"class": "header"})
    
    for text in soup.strings:
        print text
        return text
    
    
        
        

def movie_showtimes(html):
    """
    Scrapes movie showtimes for regular, 3D and Imax
    
    issue: It only scrapes the first set of movie times...
    """
    
    soup = BeautifulSoup(html)
    soup = soup.find_all("div", {"class": "showtimes"})
    
    # put the shotimes in a list
    stack = []
    
    for stuff in soup:
        
        times = showtimes(stuff)
        stack.append(times)
        
    return stack

def showtimes(html):
    """
    parses movie times
    """    
    times = re.compile('data-displaytimes="(.*)" data-logo-url')
    times = re.findall(times, str(html))
    
    # formating showtimes
    try:
        times = times[0].replace("|", "    ")
    except:
        pass
    return times

def movie_categories(html):
    """
    Scrapes movie categories
    """
    soup = BeautifulSoup(html)
    soup = soup.find("p", {"class":"cert-runtime-genre"})
    
    # will hold the movie times
    stack = []
    
    # Formating it into a string
    results = ""

    for string in soup.strings:
        
        string = unicode(string).split("\n")

        for item in string:
            try:
                if item[0].isalpha():
                    
                    item = kill_whitespace(item)                    #print "category", item, "\n", "length", len(item)
                    item = str(item)
                    stack.append(item)
            except:
                pass
            
    for index in range(len(stack)):
        
        if index != len(stack)-1:
            results += stack[index]+"|"
        else:
            results += stack[index]
    
    return results
    
def kill_whitespace(text):
    """
    Removes the whitespace that is on the right side of the text.
    """
    while text[-1] == " ":
        text = text[:-1]
        
    return text
            
def movie_duration(html):
    """
    Scrapes movie duration (if it exists)
    """

    duration = re.compile('duration">(.*)<')
    duration = re.findall(duration, html)
    
    #print duration
    return duration

def movie_poster(html):
    """
    Scrapes movie poster url and rating url (if it exists)
    """
    poster = re.compile('src="(.*)" title')
    poster = re.findall(poster, html)
    
    #print poster
    return poster
        

def movie_name(html):
    """
    Scrapes movie titel
    """
    name = re.compile('alt="(.*)" height')
    name = re.findall(name, html)
    name = name[0][:-6]
    
    #print "name:", name, "\n"
    return name
    

def movie_html(soup):
    
    even = soup.find_all("div", {"class": "list_item even"})
    
    odd  = soup.find_all("div", {"class": "list_item odd"})
    
    #print even[0], "\n", odd[0], "\n\n", type(even), "\n", len(even)
    
    stack = even + odd
    
    return stack
    
if __name__ == "__main__":
    main()
