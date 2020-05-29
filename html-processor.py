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

rexp1 = re.compile(r'<title>(.+?)</title') # Ερώτημα 1
rexp2 = re.compile(r'<!--(.*?)-->',re.DOTALL) # Ερώτημα 2
rexp3 = re.compile(r'<(script|style).*?>.*?</(script|style)>',re.DOTALL) # Ερώτημα 3, μπορούμε να βάλουμε και </\1 αντί για (script|style) τη δεύτερη φορά
rexp4 = re.compile(r'<a.+?href="(.*?)".*?>(.*?)</a>',re.DOTALL) # Ερώτημα 4
rexp5a = re.compile(r'<.+?>|</.+?>',re.DOTALL) # Ερώτημα 5α, Για tag παρόμοια με <something> ... </something> και για να αφαιρεθεί το </html> στο τέλος και tag παρόμοια με αυτό
rexp5b = re.compile(r'<.+?/>',re.DOTALL) # Ερώτημα 5β, Για tag παρόμοια με < something />
rexp6 = re.compile(r'&(amp|gt|lt|nbsp);') # Ερώτημα 6
rexp7 = re.compile(r'\s+') # Ερώτημα 7


with open('testpage.txt', 'r') as f: # function για άνοιγμα του αρχείου

    contents = f.read()
    m = rexp1.search(contents)
    print(m.group(1)) # εκτύπωση τίτλου

    contents = rexp2.sub(' ', contents) # αντικατάσταση των σχολίων με κενό

    contents = rexp3.sub(' ', contents) # αντικατάσταση περιεχομένων και style, script tags με το κενό

    for m in rexp4.finditer(contents):
        print('{} {}'.format(m.group(1),m.group(2))) # επιλέγει και εκτυπώνει τα link που βρίσκονται μέσα στην κανονική έκφραση rexp4

    contents = rexp5a.sub(' ', contents) # απαλοιφή tag part 1
    contents = rexp5b.sub(' ', contents) # απαλοιφή tag part 2

    contents = rexp6.sub(repl, contents) # σντικατάσταση html entities

    contents = rexp7.sub(' ', contents) # αντικατάσταση συνεχόμενων κενών με ένα κενό

    print(contents) # Εκτύπωση όλου του κειμένου μετά τις μετατροπές
