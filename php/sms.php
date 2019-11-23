<?php session_start(); ?>
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
<title>Minh Hiếu EC</title>
<link rel="stylesheet" href="css/style.css">
</head>

<body>
 	<div id="header">
 	  <div class="wrapperheader">
    		<div class="logo">
        		<img src="logo1.png" width="450" height="80">
        	</div>   
      </div>
   </div>

  <div id="menu1">
            <nar>
 	           <ul><div class="left">
                    <li><a href="danhsach.php">DANH SÁCH</a></li>
            	    <li><a class="active" href="sms.php">HỘP THƯ ĐẾN</a></li>
                    </div>
                    <div class="right">
     	            <li><a href="#">  
									<?php
									if(isset($_SESSION['username'])){
 										   echo "xin chào <b><font size = 3 color = green>".$_SESSION['username']."</font>!</b>";
										}
									else
 									   header('Location: index.php');
									?></a>
                   </li>
                <li><a href="logout.php"><font color="red">Log out</font></a></li>
				</div>
                <div class="clear"></div>
            </ul>
           </nar>
	</div>

    <div id="wrapper"> 
    	<div class="content">
<?php
$a = $_GET["xoa"];
if($a == 1){
	echo "<font size = 5 color = green>Đã xóa sms thành công!</font>";
	}
?>
   <h1>SMS đã nhận :</h1>
<div id="sms">

<font size="5">
<?php
$path = "sms/noidung";    
$d = dir($path);
$i = 1; //khai bao bien su sung cookie
while (false !== ($entry = $d->read())) {
	$filepath = "{$path}/{$entry}";
    if(is_file($filepath)) {
    $latest_filename = substr($entry,0,-4);
	
	$mang = array();
	$myfile = fopen("sms/noidung/$entry", "r") or die("Unable to open file!");
	while(!feof($myfile)) {
		$sms = fgets($myfile);
		$mang[]=$sms;
	}
	fclose($myfile);

	
	echo '<div class="sdt">';
    echo "<font size = 5 color = white>+$latest_filename</font><br>";
	echo '</div>';
	//foreach($mang as $value)
	//		{
	//			echo $value."<br>";
	//		}

	//echo implode($mang); //chuyen doi mang thanh chuoi
	$sokitu = strlen(implode($mang));
	$vitri = strlen(implode($mang)) - 15;
	$vitrinoidung = 0 - $vitri;
	//echo $vitrinoidung;
	$noidung = substr(implode($mang),0,$vitri);
	$thoigian = substr(implode($mang),$vitri,$sokitu);
	echo '<div class="noidung">';
	echo $noidung;
	echo '</div>';
	echo '<div class="time">';
	echo '<div class="left">';

	setcookie("user$i", $latest_filename, time() +300);
	
	if($i == 1){
		echo '<a href="traloi.php?sdt=1" class="buttontl">Trả lời</a>';
		echo '<a href="xoasms.php?sdt=1" class="buttontl">Xóa</a>';
		}
	if($i == 2){
		echo '<a href="traloi.php?sdt=2" class="buttontl">Trả lời</a>';
		echo '<a href="xoasms.php?sdt=2" class="buttontl">Xóa</a>';
		}
	if($i == 3){
		echo '<a href="traloi.php?sdt=3" class="buttontl">Trả lời</a>';
		echo '<a href="xoasms.php?sdt=3" class="buttontl">Xóa</a>';
		}
	if($i == 4){
		echo '<a href="traloi.php?sdt=4" class="buttontl">Trả lời</a>';
		echo '<a href="xoasms.php?sdt=4" class="buttontl">Xóa</a>';
		}
	if($i == 5){
		echo '<a href="traloi.php?sdt=5" class="buttontl">Trả lời</a>';
		echo '<a href="xoasms.php?sdt=5" class="buttontl">Xóa</a>';
		}
	if($i == 6){
		echo '<a href="traloi.php?sdt=6" class="buttontl">Trả lời</a>';
		echo '<a href="xoasms.php?sdt=6" class="buttontl">Xóa</a>';
		}
	if($i == 7){
		echo '<a href="traloi.php?sdt=7" class="buttontl">Trả lời</a>';
		echo '<a href="xoasms.php?sdt=7" class="buttontl">Xóa</a>';
		}
	if($i == 8){
		echo '<a href="traloi.php?sdt=8" class="buttontl">Trả lời</a>';
		echo '<a href="xoasms.php?sdt=8" class="buttontl">Xóa</a>';
		}
	if($i == 9){
		echo '<a href="traloi.php?sdt=9" class="buttontl">Trả lời</a>';
		echo '<a href="xoasms.php?sdt=9" class="buttontl">Xóa</a>';
		}
	if($i == 10){
		echo '<a href="traloi.php?sdt=10" class="buttontl">Trả lời</a>';
		echo '<a href="xoasms.php?sdt=10" class="buttontl">Xóa</a>';
		}

	echo '</div>';
	echo '<div class="right">';
	echo $thoigian;
	echo '</div></div>';
	echo '<div class="clear"></div>';	
	echo "</li>";

	$i = $i + 1;    }

}
?>
</div>
</div>
<div class="clear"></div>
<div id="topfooter">
	<div class="left">SMS vừa xóa :
    <?php
	$fp ="system/smsnewdelete.txt";
	$fo = fopen($fp, 'r');
	$fr = fgets($fo);
	$fc = fclose($fo);
	echo $fr;
	?> 
    </div>
	<div class="right">
 		Time Now:
<?php
date_default_timezone_set("Asia/Ho_Chi_Minh");
$now = date("d/m/Y H:i:s"); // 26/09/2014 14:27:08
echo $now;
?>
	</div>
<div class="clear"></div>
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


