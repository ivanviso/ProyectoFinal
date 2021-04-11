import ipaddress

def ipgen(network,usedIPs) :
    hosts=list(ipaddress.ip_network(network).hosts())
    for ip in hosts :
        if ip not in usedIPs:
            return ip
