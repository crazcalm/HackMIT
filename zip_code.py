import urllib
from bs4 import BeautifulSoup

def main(geolocation):
    """
    JS will send the geolocation data here and  then
    we will use that data to find the zip code that 
    cooresponds to that location.
    """
    
    if len(geolocation) != 2:
        
        # My home geolocation
        print "Geolocation was not passed to the function..."
        
        latitude  = "40.523572"
        longitude = "-74.465806"
        
    else:
        # geolocation from JS
        latitude  = geolocation[0]
        longitude = geolocation[1]
    
    url = "http://geocoder.ca/?moreinfo=1&latt=" + latitude +"&longt=" + longitude +"&reverse=Reverse+GeoCode"
    
    soup = create_soup(url)
    
    zip = parse_zip_code(soup)
    
    return zip
    
def parse_zip_code(soup):
    """
    This will parse the html and find the zip code
    """
    #parses for the zip code
    zip_code = soup.find_all("a")
    zip_code = str(zip_code[10]).split(">")[1].split(" ")[0]
    
    
    print zip_code
    return zip_code
    
def create_soup(url):
    """
    Goes to a web page and makes it into BeautifulSoup soup
    """
    html = urllib.urlopen(url)
    content = html.read()
    soup = BeautifulSoup(content)
    
    #print soup.prettify()
    return soup
    
    
if __name__ == "__main__":
    main()
