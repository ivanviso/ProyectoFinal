<?php
$private_key = shell_exec('wg genkey');
$public_key = shell_exec("echo '$private_key' | wg pubkey");

// cliente
$client_conf= " 
[Interface]
PrivateKey = $private_key
Address = 100.0.0.2/32
DNS = 8.8.8.8

[Peer]
PublicKey = K4haGkC6bMpg+gclHTMxlEIQUzkGogRCXRLbV2nxcTQ=
AllowedIPs = 0.0.0.0/1, 128.0.0.0/1
Endpoint = 40.117.235.76:55555
";


$client_conf=preg_replace('/[\r\n]+/', "\n", $client_conf);
$client_conf=preg_replace('/[ \t]+/', ' ', $client_conf);
echo $client_conf;

?>