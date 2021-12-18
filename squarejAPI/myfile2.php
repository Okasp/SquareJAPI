<?php
$db = "test2";
$mysql_user="root";
$mysql_pass="";
$host = "localhost";

$user = $_POST["user"];
$pass = $_POST["pass"];
	
$conn = mysqli_connect($host,$mysql_user,$mysql_pass,$db);
if($conn) 
{
$sql="insert into user(user,pass) values('".$user."','".$pass."')";
	if($result=mysqli_query($conn,$sql))
	{
		echo "data inserted";
	}
	else
	{
		echo "data not inserted";
	}
} else {

	echo "Not connected!";
}	
	
	
	
?>
