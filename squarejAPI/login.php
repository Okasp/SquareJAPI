<?php
$db = "test2";
$user = $_POST["user"];
$pass = $_POST["pass"];
$host = "localhost";

$conn = mysqli_connect($host, $user, $pass, $db);
if($conn) 
{
$q = "select * from user where user like '$user' and
	pass like '$pass'";
	$result = mysqli_query($conn, $q);
if (mysqli_num_rows($result) > 0)
{
	echo "login successful...!";
} else {
echo "login failed...!";	
}	


}else
{
	echo "Not Connected....!";
}

?>
