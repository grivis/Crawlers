import urllib.request
doc = urllib.request.urlopen("http://mosyabloko.ru")
print(doc.info())
