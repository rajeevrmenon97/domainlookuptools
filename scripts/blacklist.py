import dns.resolver
import dns.reversename

blacklists = {
        'Webiron LLC RBL'           : 'all.rbl.webiron.net',
        'Webiron LLC RBL Crawler '  : 'crawler.rbl.webiron.net',
        'ARM Research Labs, LLC'    : 'truncate.gbudb.net',
        'UCEPROTECT Level 1'        : 'dnsbl-1.uceprotect.net',
        'UCEPROTECT Level 2'        : 'dnsbl-2.uceprotect.net',
        'UCEPROTECT Level 3'        : 'dnsbl-3.uceprotect.net',
	'SORBS dnsbl'               : 'dnsbl.sorbs.net',
        'SORBS safe.dnsbl'          : 'safe.dnsbl.sorbs.net',
        'SORBS http.dnsbl'          : 'http.dnsbl.sorbs.net',
        'SORBS socks.dnsbl'	    : 'socks.dnsbl.sorbs.net',
        'SORBS misc.dnsbl'          : 'misc.dnsbl.sorbs.net',
        'SORBS smtp.dnsbl'          : 'smtp.dnsbl.sorbs.net',
        'SORBS web.dnsbl'           : 'web.dnsbl.sorbs.net',
        'SORBS new.spam.dnsbl'      : 'new.spam.dnsbl.sorbs.net',
        'SORBS recent.spam.dnsbl'   : 'recent.spam.dnsbl.sorbs.net',
        'SORBS old.spam.dnsbl'      : 'old.spam.dnsbl.sorbs.net',
        'SORBS spam.dnsbl'          : 'spam.dnsbl.sorbs.net',
        'SORBS escalation.dnsbl'    : 'escalations.dnsbl.sorbs.net',
        'SORBS block.dnsbl'         : 'block.dnsbl.sorbs.net',
        'SORBS zombie.dnsbl'        : 'zombie.dnsbl.sorbs.net',
        'SORBS dul.dnsbl'           : 'dul.dnsbl.sorbs.net',
        'SORBS noservers.dnsbl'     : 'noservers.dnsbl.sorbs.net',
        'SORBS rhsbl'               : 'rhsbl.sorbs.net',
        'SORBS badconf.rhsbl'       : 'badconf.rhsbl.sorbs.net',
        'SORBS nomail.rhsbl'        : 'nomail.rhsbl.sorbs.net',
        'Spamhaus Zen'              : 'zen.spamhaus.org',
        'CBL'                       : 'cbl.abuseat.org',
        'Cobion IBM DNS Blacklist'  : 'dnsbl.cobion.com',
        'PSBL'                      : 'psbl.surriel.com',
        'DNSRBL'                    : 'dnsrbl.org',
        'WPBL'                      : 'db.wpbl.info',
        'RBL'                       : 'bad.psky.me',
        'SCBL'                      : 'bl.spamcop.net',
        'SpamRats NoPtr'            : 'noptr.spamrats.com',
        'SpamRats Dyna'             : 'dyna.spamrats.com',
        'SpamRats Spam'             : 'spam.spamrats.com',
        'SpamRats Auth'             : 'auth.spamrats.com',
        'SpamCannibal'              : 'bl.spamcannibal.org',
        'NiX Spam'                  : 'ix.dnsbl.manitu.net',
        'inps.de-DNSBL'             : 'dnsbl.inps.de',
        'blocklist.de'              : 'bl.blocklist.de',
        'SRN'                       : 'srnblack.surgate.net',
        's5h.net Internet Services' : 'all.s5h.net',
        'MegaRBL'                   : 'rbl.megarbl.net',
        'realtimeBLACKLIST.com'     : 'rbl.realtimeblacklist.com',
        'BarracudeCentral'          : 'b.barracudacentral.org',
        }

class blacklist_record(object):
    def __init__(self):
        self.status = " "
        self.blacklist = " "
        self.address = " "
        self.ttl = -1
        self.txt = " "

def check_dnsbl(addr, bl):
    rec = blacklist_record()
    rec.status = "OK"
    rev = dns.reversename.from_address(addr)
    domain = str(rev.split(3)[0]) + '.' + bl
    try:
        r = dns.resolver.query(domain, 'a')
    except (dns.resolver.NXDOMAIN, dns.resolver.NoNameservers, dns.resolver.NoAnswer):
        return rec
    rec.address = list(r)[0].address
    rec.ttl = r.ttl
    try:
        r = dns.resolver.query(domain, 'txt')
        rec.txt = list(r)[0].to_text()
    except (dns.resolver.NoAnswer, dns.resolver.NXDOMAIN):
        rec.txt = ' '
    rec.status = "LISTED"
    return rec

def getRecord(domain,flag=True):
    answer = []
    if flag:
        try:
            a = dns.resolver.query(domain,"A")
            ip = a[0].address
        except:
            return None
    else:
        ip = domain
    for i in blacklists:
        temp = check_dnsbl(ip,blacklists[i])
        temp.blacklist = i
        answer.append(temp)
    answer.sort(key=lambda x: x.status)
    return answer

def out(rec):
    for r in rec:
        print "{:6s} {:28s} {:16s} {:5d} {:s}".format(r.status,r.blacklist,r.address,r.ttl,r.txt)
