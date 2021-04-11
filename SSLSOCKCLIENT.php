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
$loginstep="auth";
echo "\n";
$username="ivanviso123@gmail.com";
$password="abcABC123";
if ($socket = stream_socket_client(
        'tls://'.$host.':'.$port,
        $errno,
        $errstr,
        30,
        STREAM_CLIENT_CONNECT,
        $context)
    ) {
        
        if ($loginstep=="auth") {
            echo $loginstep;
            fwrite($socket,"AUTH");
            $reply=fread($socket,64);
            echo $reply,"\n";
        }
        if ($reply="OK AUTH") { 
            $loginstep="user";
        }
        if ($loginstep="user") {
            fwrite($socket,"USER ".$username);
            $reply=fread($socket,7);
            echo $reply,"\n";
        }
        if ($reply="OK USER") { 
            $loginstep="pass";
        }
        if ($loginstep="pass") {
            fwrite($socket,"PASS ".$password);
            $reply=fread($socket,7);
            echo $reply,"\n";
            $loginstep="fin";
            
        }
        if ($loginstep="fin") {
            $reply=fread($socket,4096);
            echo $reply,"\n";

        }





    }
 else {
   echo "ERROR: $errno - $errstr\n";
}
fclose($socket);
?>