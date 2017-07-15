
import dns.resolver
import dns.reversename
import geocoder

class ptr_record(object):
    def __init__(self):
        self.ip = " "
        self.location = "-"
        self.domain = "-"
        self.ttl = -1

def getRecord(ip):
    try:
        rev = dns.reversename.from_address(ip)
    except:
        return None
    answer = ptr_record()
    try:
        dom = dns.resolver.query(rev,"PTR")
        answer.domain = dom[0].to_text()[:len(dom[0].to_text())-1]
        answer.ttl = dom.ttl
        answer.ip = ip
        answer.location = geocoder.ip(ip).address
    except:
        return None
    return answer
