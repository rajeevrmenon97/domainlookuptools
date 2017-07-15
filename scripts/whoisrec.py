import whois
import re

class whois_record(object):
    def __init__(self):
        self.table = []
        self.raw = ' '

def getRecord(domain):
    try:
        w = whois.whois(domain)
    except:
        return None
    m = re.findall('([A-Z][a-z].*): (.*)',w.text)
    if m:
        m.pop()
    answer = whois_record()
    answer.table = m
    answer.raw = w.text
    return answer
