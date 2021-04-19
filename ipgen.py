import ipaddress

def ipgen(network,usedIPs) :
    usedipobj=list()
    for ip in usedIPs :
        for ip2 in ip :
            usedipobj.append(ipaddress.ip_address(ip2))
    print(usedipobj)
    for ip in ipaddress.ip_network(network).hosts():
        if ip not in usedipobj:
            print(int(ip))
            return int(ip)
            

