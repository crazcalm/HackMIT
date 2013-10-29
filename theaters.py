from bs4 import BeautifulSoup
from zip_code import create_soup

def main(zip_code = "08904"):
    """
    Just give me the first five theaters in my area.
    """
    
    url = "http://www.imdb.com/showtimes/cinemas/US/" + zip_code
    
    soup = create_soup(url)
    
    theater = five_miles_theaters(soup)
    even, odd = theaters_even_odd(theater)
    theater = theaters(soup, even, odd)
    
    cinema = theater_info(theater)
    """
    print "\n\n\n", "Cinema info: ", cinema, "\n\n"
    
    for x in cinema:
        print "Spacing \n\n"
        for key in x:
            
            print key, x[key]
    """
    #print type(theater), "\n\n", len(theater), "\n\n", theater[0]

    return cinema
    
def five_miles_theaters(soup):
    """
    Obtain the number of movie theaters within 5 mile
    """

    # finds the html tag/ class for the movies within five miles (list)
    five_miles = soup.find_all("h4", {"class": "li_group"}, limit = 2)

    # parses the string to find the number of theater within 5 miles.
    five_miles = str(five_miles[0]).split("(")[1].split(")")[0]
    
    #print "five_miles variable",five_miles
    five_miles = int(five_miles) 
    
    return five_miles

"""

Gaol 1.5: make sure that I am never scraping more that 4 theaters.

"""

def theater_limit(number):
    """
    Makes sure that I am scraping 4 or less theaters.
    """
    limit = 4
    
    if number > limit:
        number = limit
    else:
        pass
    
    #print "theater_limit:", number
    return number

"""

Goal 2: Calculating the number of Theaters that I want to look at in terms of even and odd.

"""

def theaters_even_odd(total): #works
    """
    Calulates the number of even and odd theaters that I want to look at.
    """
    
    even = total / 2 # Works because it is int division
    odd  = total  - even # If you are not even, then you are odd.
    
    #print "even and odd:",even, odd, "\n"
    return even, odd


"""

Goal 3: obtaining the html of the theaters that I want.

"""

def theaters(soup , even, odd): # works
    """
    Gets the info from the theater section
    """
    even_theaters = soup.find_all("div", {"class":"list_item even"}, limit = even)
    
    odd_theaters = soup.find_all("div", {"class":"list_item odd"}, limit = odd)
    
    theaters  = odd_theaters + even_theaters
    
    return theaters

def theater_info(theaters):
    """
    Scrapes the info that I want from the theaters
    """
    
    # All theater info goes into a list.
    all_theater_info = []
    
    # I would like to know what theater index we are on
    count = 0
    
    # Later: change to all theaters
    for theater in theaters:
        
        count+=1
        print "Theater index:", count
        
        theater_info = theater.find_all("h3", limit =3)
        
        # parsing theater website
        web_site =  "http://www.imdb.com/" + str(theater_info[0]).split(">")[1].split(" ")[1].split("=")[1][1:-1]
        
        # Parsing for the theater name
        theater_name = str(theater_info[0]).split(">")[2].split("<")[0]
    
    
        theater_info = theater.find_all("span", limit =6)
        
        # holds theater address
        address = ""
        
        for item in theater_info[:4]:
            address += str(item).split(">")[1].split("<")[0] + " "
        
        # phone number    
        phone_num = str(theater_info[5]).split(">")[1].split("<")[0]
        
        # all individal theater info goes here
        """
        one_theater_info = []
        # Adding info to list
        one_theater_info.append(theater_name)
        one_theater_info.append(address)
        one_theater_info.append(phone_num)
        one_theater_info.append(web_site)
        """
        
        one_theater_dict = {"name":theater_name, "address": address, "number": phone_num,"web_site":web_site}
    
        all_theater_info.append(one_theater_dict)
        
    return all_theater_info


if __name__ == "__main__":
    main()
