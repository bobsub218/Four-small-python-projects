from sys import argv 
#from sys import argv 
#Generally, the first argument to a command-line executable is the script name, and the rest are the expected arguments.
#Here, is a list that is expected to contain two values: the script name and an argument. Using Python's unpacking notation, you can writeargv

import urllib #urllib.request is a Python module for fetching URLs

from bs4 import BeautifulSoup #In Python 3.x, the raise Exception, "foo" syntax is no longer supported. So you need to install a version of BeautifulSoup that supports Python 3, so install (pip install beautifulsoup4)
import datetime
def ShowHelp():
    print ('Insta Image Downloader')
    print ('')
    print ('Usage:')
    print ('insta.py [OPTION] [URL]')
    print ('')
    print ('Options:')
    print ('-u [Instagram URL]\tDownload single photo from Instagram URL')
    print ('-f [File path]\t\tDownload Instagram photo(s) using file list')
    print ('-h, --help\t\tShow this help message')
    print ('')
    print ('Example:')
    print ('python insta.py -u https://instagram.com/p/xxxxx')
    print ('python insta.py -f /home/username/filelist.txt')
    print ('')
    exit()
def DownloadSingleFile(fileURL):
    print ('Downloading image...')
    f = urllib.urlopen(fileURL)
    htmlsource = f.read()
    soup = BeautifulSoup(htmlsource,'html.parser')
    metaTag = soup.find_all('meta', {'property':'og:image'})
    imgURL = metaTag[0]['content']
    fileName = datetime.datetime.now().strftime("%Y-%m-%d_%H:%M:%S") + '.jpg'
    urllib.urlretrieve(imgURL, fileName)
    print ('Done. Image saved to disk as ' + fileName)
if __name__ == '__main__':
    if len(argv) == 1:
        ShowHelp()
    if argv[1] in ('-h', '--help'):
        ShowHelp()
    elif argv[1] == '-u':
        instagramURL = argv[2]
        DownloadSingleFile(instagramURL)
    elif argv[1] == '-f':
        filePath = argv[2]
        ph = open(filePath)
        line = ph.readline()
        while line:
            instagramURL = line.rstrip('\n')
            DownloadSingleFile(instagramURL)
            line = ph.readline()
        ph.close()