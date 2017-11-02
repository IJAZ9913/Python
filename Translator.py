#Coded by The Alien
import string,os
os.system("clear")
def banner():
    print """\t _ _______________
\t/ |___ /___ /___  |
\t| | |_ \ |_ \  / /
\t| |___) |__) |/ /
\t|_|____/____//_/ Translator
\t\tBy The Alien | P.C.G."""

def translator(a):
    text = a
    lower= string.maketrans("abeiost","4831057")
    upper= string.maketrans("ABEIOST","4831057")
    t_text = text.translate(lower)
    t_text = t_text.translate(upper)
    print "\n\n\rTranslated Text: %s" % (t_text)

banner()
a = raw_input("Enter Text: ")
translator(a)
