<?php
session_start(); //Tim session
$_SESSION = array(); // huy tat ca cac bien cua session

//bo tat ca cac cookies
if(isset($_COOKIE[session_name()])){
    setcookie(session_name(), time()-36000,'/',0,0);
}
//huy toan bo session
session_destroy();
header('Location: index.php?stat=1'); //chuyen ve trang dang nhap
?>
