import urllib.request  # импортируем модуль
import re
# req = urllib.request.Request('https://habrahabr.ru/')
# with urllib.request.urlopen(req) as response:
#    html = response.read().decode('utf-8')
# print(html[:250])

url = 'https://habrahabr.ru/'  # адрес страницы, которую мы хотим скачать
user_agent = 'Mozilla/5.0 (Windows NT 6.1; Win64; x64)'  # хотим притворяться браузером

req = urllib.request.Request('https://habrahabr.ru/', headers={'User-Agent':user_agent})
# добавили в запрос информацию о том, что мы браузер Мозилла

with urllib.request.urlopen(req) as response:
   html = response.read().decode('utf-8')


regPostTitle = re.compile('<h2 class="post__title">.*?</h2>', flags=re.U | re.DOTALL)
titles = regPostTitle.findall(html)


print(len(titles))
#print(titles[:3])

new_titles = []
regTag = re.compile('<.*?>', flags=re.U | re.DOTALL)
regSpace = re.compile('\s{2,}', flags=re.U | re.DOTALL)
for t in titles:
    clean_t = regSpace.sub("", t)
    clean_t = regTag.sub("", clean_t)
    new_titles.append(clean_t)
# for t in new_titles:
#     print(t)


for t in new_titles:
    print(t.replace("&nbsp;&rarr;", " -> "))