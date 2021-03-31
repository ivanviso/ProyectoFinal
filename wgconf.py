listen_addr="127.0.0.1"
server_port="12345"
address="192.168.1.1"
address_ipv6=f"fc00:abcd:abcd:abcd::{address}"

def clientwgconf(public_key,private_key):
    conf = f"""
    [Interface]
    Address = {address} {address_ipv6}
    PrivateKey = {private_key}

    [Peer]
    Address= {address}
    Endpoint = {listen_addr}:{server_port}
    PublicKey = {public_key}
    """
    return conf