import dns.resolver
import geocoder
import ptr

class ipaddress(object):
    def __init__(self):
        self.address = " "
        self.location = " "
        self.ptr = " "

class a_record(object):
    def __init__(self):
        self.domain = " "
        self.ip = []
        self.ttl = -1
        self.num = 0

def getAddress(ip):
    try:
        location = geocoder.ip(ip)
    except:
        return None
    return location.address

def getRecord(domain,ip_version="ipv4"):
    if(ip_version=="ipv4"):
        q = "A"
    elif(ip_version == "ipv6"):
        q = "AAAA"
    else:
        return None
    try:
        records = dns.resolver.query(domain,q)
    except:
        return None
    answer = a_record()
    answer.domain = domain
    answer.ttl = records.ttl
    iplist = []
    for rec in records:
        temp = ipaddress()
        temp.address = rec.to_text()
        temp.location = getAddress(temp.address)
        try:
            temp.ptr = ptr.getRecord(temp.address).domain
        except:
            temp.ptr = ' '
        iplist.append(temp)
    answer.ip = iplist
    answer.num = len(iplist)
    return answer

def out(rec):
    if type(rec) is not a_record:
        return
    else:
        for i in rec.ip:
            print "{:30s} {:16s} {:50s} {:d}".format(rec.domain,i.address,i.location,rec.ttl)
        return
