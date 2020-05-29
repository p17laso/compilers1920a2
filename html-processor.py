import re

def repl(m): # replace function
    if(m.group(0)=='&amp;'):
        return '&'
    elif(m.group(0)=='&gt;'):
        return '>'
    elif(m.group(0)=='&lt;'):
        return '<'
    else:
        return ' '

rexp1 = re.compile(r'<title>(.+?)</title') # Erwthma 1
rexp2 = re.compile(r'<!--(.*?)-->',re.DOTALL) # Erwthma 2
rexp3 = re.compile(r'<(script|style).*?>.*?</(script|style)>',re.DOTALL) # Erwthma 3, mporoyme na valoyme kai </\1 anti gia (script|style) th deyterh fora
rexp4 = re.compile(r'<a.+?href="(.*?)".*?>(.*?)</a>',re.DOTALL) # Erwthma 4
rexp5a = re.compile(r'<.+?>|</.+?>',re.DOTALL) # Erwthma 5a, gia tag paromoia me <something> ... </something> kai gia na afairethei to </html> sto telos toy txt arxeioy kathws kai tag paromoia me ayto
rexp5b = re.compile(r'<.+?/>',re.DOTALL) # Erwthma 5b, gia tag paromoia me < something />
rexp6 = re.compile(r'&(amp|gt|lt|nbsp);') # Erwthma 6
rexp7 = re.compile(r'\s+') # Erwthma 7


with open('testpage.txt', 'r') as f: # function gia anoigma toy arxeioy

    contents = f.read()
    m = rexp1.search(contents)
    print(m.group(1)) # ektypwsh titloy

    contents = rexp2.sub(' ', contents) # antikatastash twn sxoliwn me keno

    contents = rexp3.sub(' ', contents) # antikatastash twn periexomenwn kai style, script tags me to keno

    for m in rexp4.finditer(contents):
        print('{} {}'.format(m.group(1),m.group(2))) # epilegei kai ektypwnei ta links poy vriskontai mesa sthn kanonikh ekfrash rexp4

    contents = rexp5a.sub(' ', contents) # apaloifh tag part 1
    contents = rexp5b.sub(' ', contents) # apaloifh tag part 2

    contents = rexp6.sub(repl, contents) # antikatastash html entities

    contents = rexp7.sub(' ', contents) # antikatastash synexomenwn kenwn me ena keno

    print(contents) # ektypwsh oloy toy keimenoy meta tis metatropes
