<?PHP
$host = 'socket.local';
$port = 8082;
$timeout = 3;
$cert = 'client.crt'; // Path to certificate
$key = 'client.key';
$email = "pepe";
$context = stream_context_create(
    array('ssl'=>array('local_cert'=>$cert,'local_pk'=>$key,'allow_self_signed'=>true))
    );
    while(true) {
        $numb=rand();
        sleep(1);
if ($socket = stream_socket_client(
        'tls://'.$host.':'.$port,
        $errno,
        $errstr,
        30,
        STREAM_CLIENT_CONNECT,
        $context)
    ) {
 
        fwrite($socket,$numb);
        echo fread($socket,4096),"\n";
    
    }
 else {
   echo "ERROR: $errno - $errstr\n";
}
fclose($socket);

}
?>