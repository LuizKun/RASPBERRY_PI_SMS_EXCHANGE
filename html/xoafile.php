        <?php
$a = $_GET["sdt"];
if($a == 1){
	$sdt = $_COOKIE["user1"];
}
if($a == 2){
	$sdt = $_COOKIE["user2"];
}
if($a == 3){
	$sdt = $_COOKIE["user3"];
}
if($a == 4){
	$sdt = $_COOKIE["user4"];
}
if($a == 5){
	echo $_COOKIE["user5"];
}
if($a == 6){
	echo $_COOKIE["user6"];
}
if($a == 7){
	echo $_COOKIE["user7"];
}
if($a == 8){
	echo $_COOKIE["user8"];
}
if($a == 9){
	echo $_COOKIE["user9"];
}
if($a == 10){
	echo $_COOKIE["user10"];
}
?>
<?php
unlink("upload/".$sdt);
$delete = "system/filenewdelete.txt";
$deleteopen = fopen($delete, 'w');
$deletewrite = fwrite($deleteopen, $sdt);
$deleteclose = fclose($deleteopen);
header('Location: danhsach.php?xoa=1');
?>