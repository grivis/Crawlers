import urllib.request

def download_page(pageUrl):
    try:
        page = urllib.request.urlopen(pageUrl)
        text = page.read().decode('ISO-8859-1')
    except:
        print('Error at', pageUrl)
        return
    # do something with the downloaded text

commonUrl = 'http://www.forumishqiptar.com/threads/'
for i in range(160400, 160425):
    pageUrl = commonUrl + str(i)
    download_page(pageUrl)