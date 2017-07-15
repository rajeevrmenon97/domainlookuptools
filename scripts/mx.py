import dns.resolver
import a
import ptr

class mx_record(object):
    def __init__(self):
        pref = -1
        hostname = ' '
        ip = a.ipaddress()
        location = ' '
        ttl = -1

def getRecord(domain):
    try:
        records = dns.resolver.query(domain,"MX")
    except:
        return None
    answer = []
    for rec in records:
        mx4 = mx_record()
        mx6 = mx_record()
        mx4.ttl = mx6.ttl = records.ttl
        temp = rec.to_text().split(" ", 1)
        mx4.pref = mx6.pref = temp[0]
        mx4.hostname = mx6.hostname = temp[1][:len(temp[1])-1]
        temp = a.getRecord(mx4.hostname,"ipv4")
        if temp is not None:
            mx4.ip = temp.ip
            answer.append(mx4)
        temp = a.getRecord(mx6.hostname,"ipv6")
        if temp is not None:
            mx6.ip = temp.ip
            answer.append(mx6)
    answer.sort(key=lambda x: x.pref)
    return answer

def out(rec):
    if type(rec) is not list:
        return
    else:
        for i in rec:
            for j in i.ip:
                print "{:5s} {:30s} {:30s} {:65s} {:d}".format(i.pref,i.hostname,j.address,j.location,i.ttl)
        return
