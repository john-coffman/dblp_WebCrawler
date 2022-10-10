import os
import time
import random


def makeUrl(pid, page):
    rurl = ' https://dblp.org/pid/' + str(pid) + '/' + str(page) + '.html'
    return rurl

def makeOutput(num_page):
    output = ' > holder1/page' + str(num_page) + '.txt'
    return output

count = 1
pid = 97
page = 6063
output = ' > holder1/page.txt'
L = ' -L'
m = ' -m 10'
h1 = ' -H "Accept: application/json, text/javascript, */*; q=0.01"'
h2 = ' -H "Accept: Encoding:"'
h3 = ' -H "Accept: Language: en us, en; q=0.5"'
h4 = ' -H "Connection: keep alive"'
e = ' -e https://dblp.org/'
error = ' --stderr errorFile.txt'
user = ' --user-agent "Mozilla/5.0 (X11; Linux x86_64; rv:10.0.3) Firefox/10.0.3"'

while(count <= 20):
    if(count == 1):
        cookie = ' -c "cookiefile.txt"'
        rurl = makeUrl(pid, page)
    else:
        cookie = ' -b "cookiefile.txt"'
        r1 = random.randint(1, 10)
        r2 = random.randint(1, 100)
        pid += r1
        page += r2
        rurl = makeUrl(pid, page)
    output = makeOutput(count)
    cmd = "curl" + cookie + L + m + h1 + h2 + h3 + h4 + e + error + user + rurl + output
    os.system(cmd)
    count += 1
    time.sleep(10)






