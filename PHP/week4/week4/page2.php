<?php
    session_start();

    if(isset($_COOKIE['cookie_name'])){
        $output = $_COOKIE['cookie_name'];
    }elseif($_SESSION['mysesh'] != null){
        $output = $_SESSION['mysesh'];
    }else{
        header('location: week4.php');
    }


?>
<!DOCTYPE html>
<html>
<body>

<h1>This is page 2</h1>
<p>Your cookie/session is <?php echo $output ?>
<br>
<a href="week4.php?">Go Back </a>
</body>
</html>