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
    	           	<li><a href="thongbao.php">HOME</a><li>
        	        <li><a href="danhsach.php">DANH SÁCH</a></li>
            	    <li><a class="active" href="upload.php">UPLOAD</a></li>
 	                <li><a href="sms.php">TIN NHẮN</a></li>
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
    <h1>UPLOAD FILE</h1>
<p>
<form method="post" enctype="multipart/form-data">
<input type="file" name="fileupload" />
<input type="submit" name="submit_name" value="Upload File" />
</form>
<?php
//khai bao duong dan tam cho file upload
$link_temp = $_FILES["fileupload"]["tmp_name"];
//khai bao ten file
$file_name = $_FILES["fileupload"]["name"];
//khai bao kieu file
$file_type = $_FILES["fileupload"]["type"];
//khai bao size file
$file_size = $_FILES["fileupload"]["size"];
//thong bao loi trong qua trinh upload
$file_error = $_FILES["fileupload"]["error"];
//Khai bao duong dan moi

if(file_exists("upload/$file_name"))
	{
 			$kiemtrafile = 1;
	}
else{
	$new_link = "upload/".$file_name;
	move_uploaded_file($link_temp, $new_link);
}//end els
?>
<?php
$sub = $_POST["submit_name"];
if($sub == "Upload File"){
  if($kiemtrafile == 1){
	  $kiemtrafile = 0;
	 echo "<font size = 5 color = red>File đã tồn tại, vui lòng xóa hoặc chọn file khác!</font>"; 
	  }
  else{
	if($file_error == 0)
	{
		echo "<font size = 5 color = green>Upload file thành công!</font><br>";
		echo "File Name :".$file_name."<br>";
		$kichthuoc = $file_size/1024;
		echo "File Size :".$kichthuoc." Kb<br>";
		echo "File Type :".$file_type."<br>";
		
			$filenew = "system/filenewupload.txt";
			$filenewopen = fopen($filenew, 'w');
			$filenewwrite = fwrite($filenewopen, $file_name );
			$filenewclose = fclose($filenewopen);
	}
		if($file_error == 1){
			echo "<font size = 5 color = red>Dung lượng File vượt quá cho phép!</font><br>";
			}
		if($file_error == 2){
			echo "<font size = 5 color = red>Dung lượng File vượt quá cho phép của cấu hình hệ thống!</font><br>";
			}
		if($file_error == 3){
			echo "<font size = 5 color = red>File chỉ được tải lên một phần!</font><br>";
			}
		if($file_error == 4){
			echo "<font size = 5 color = red>Không có File nào được tải lên hoặc File không tồn tại!</font><br>";
			}
  }
}//end if submit
?>

</div>
</div>
<div class="clear"></div>
<div id="topfooter">
<div class="left">File vừa tải lên: 
<?php
$fp ="system/filenewupload.txt";
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

