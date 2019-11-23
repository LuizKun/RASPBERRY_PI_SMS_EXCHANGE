<?php session_start(); ?>
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
<title>Minh Hiếu EC</title>
<link rel="stylesheet" href="css/styleweb.css">
</head>

<body>
 	<div id="header">
 	  <div class="wrapperheader">
    	<div class="logo">
        <img src="logo1.png" width="450" height="80">
        </div>   
            <div class="menu">
             </div>
            <div class="clear"></div>
		</div></div>

  <div id="menu1">
            <nar>
            <ul><div class="left">
               	<li><a class="active" href="#">HOME</a></li>
                <li><a href="#">DANH SÁCH</a></li>
                <li><a href="#">UPLOAD</a></li>
                <li><a href="#">ABOUT</a></li>
                </div>
                <div class="right">
                <li><a href="#">ĐĂNG NHẬP</a></li>
                <li><a href="#">ĐĂNG KÝ</a></li>
				</div>
            </ul>
            </nar>
</div>

    </header>    
    <div id="wrapper">    
    <?php
	if (isset($_SESSION['username'])){
     		 header('Location: danhsach.php');
      		 }
        if(isset($_POST['submit'])){
           $user1 = $_POST['user'];
	   $pass1 = $_POST['pass'];
	}
	if($user1 == "admin" && $pass1 == "222333"){
	$_SESSION['username']=$_POST['user'];
	header('Location: danhsach.php');
	}
	else 
            $kiemtra = 1;
if(isset($_GET['stat']) && $_GET['stat'] == 1){
        $massage = "<font color = green>Bạn đã log out thành công!</font>";
        }
?>

    <div class="login-page">
<div class="form">
<font size ='5' color="blue"><b>LOG IN</b></font>
<form class="login-form" method="POST" action="index.php">
    <input type="text" name="user" placeholder="username"/><br />
    <input type="password" name="pass" placeholder="password"/><br/>
    <input type="submit" name="submit" value="Login"/>
    <?php
     if(isset($_POST['submit']) && $kiemtra == 1){
       echo "<font color = red>Đăng nhập thất bại</font>";
       }
       if(isset($massage)){
         echo $massage;   
        }
    ?>
</form>
</div>
</div>
<div class="clear"></div>
 </div>
<div id="topfooter"> Time :
<?php
date_default_timezone_set("Asia/Ho_Chi_Minh");
$now = date("d/m/Y H:i:s"); // 26/09/2014 14:27:08
echo $now;
?>
</div>
	<div id="footer">
		<font color="blue" size="+3"><b>TRƯỜNG ĐẠI HỌC VĂN HIẾN</b></font>
		<br />
		<font color="green" size="+2">KHOA KỸ THUẬT - CÔNG NGHỆ
		</font><BR />
		NGUYỄN MINH HIẾU- <i>THIẾT KẾ HỆ THỐNG TỔNG ĐÀI SINH VIÊN.</i> <br />
	</div>
</div>
</body>
</html>

