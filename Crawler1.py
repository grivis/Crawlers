import urllib.request
import re
import html

def download_page(pageUrl):
    try:
        page = urllib.request.urlopen(pageUrl)
        text = page.read().decode('utf8')
    except:
        print('Error at', pageUrl)
        return
    finally:
        return text
        # do something with the downloaded text

#commonUrl = 'http://www.forumishqiptar.com/threads/'
commonUrl = 'http://forum-moskva.ru/viewtopic.php?f=159&t=1130/'

# for i in range(160400, 160425):
#     pageUrl = commonUrl + str(i)
#     download_page(pageUrl)
print('Первая страница')
pagetxt = download_page(commonUrl)
#print(pagetxt)

html_content = '<html>....</html>'  # тут какой-то html

regTag = re.compile('<.*?>', flags=re.U | re.DOTALL)  # это рег. выражение находит все тэги
regScript = re.compile('<script>.*?</script>', flags=re.U | re.DOTALL) # все скрипты
regComment = re.compile('<!--.*?-->', flags=re.U | re.DOTALL)  # все комментарии

# а дальше заменяем ненужные куски на пустую строку
clean_t = regScript.sub("", pagetxt)
clean_t = regComment.sub("", clean_t)
clean_t = regTag.sub("", clean_t)

#print(clean_t)


print( html.unescape(clean_t) )

# print('Вторая страница')
# commonUrl = 'http://forum-moskva.ru/viewtopic.php?f=159&t=29878'
# pagetxt = download_page(commonUrl)
# print(pagetxt)