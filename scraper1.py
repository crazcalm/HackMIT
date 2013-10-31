"""
You are now my testing ground!
"""

"""
I need to download the photos so that I can use them...
"""
import urllib, os

def download_img(url_list, name):
    """
    download a comic in the form of

    url = http://www.example.com
    comicName = '00000000.jpg'
    """
    
    current_dir = os.getcwd()
    #print current_dir
    
    new_dir = os.chdir(current_dir+"/static/img")
    #print "Current dir: ",os.getcwd()
    
    
    for index in range(len(url_list)):
        if index == 0:
            name1 = str(name)+".jpg"
            if not os.path.exists(name1):
    
                image=urllib.URLopener()
                image.retrieve(url_list[index], filename = name1)  # download comicName at URL

        if index == 1:
            name2 = str(name)+".png"
            if not os.path.exists(name2):
    
                image=urllib.URLopener()
                image.retrieve(url_list[index], filename = name2)  # download comicName at URL
    
    os.chdir(current_dir)
    


if __name__ == "__main__":
    download_img()