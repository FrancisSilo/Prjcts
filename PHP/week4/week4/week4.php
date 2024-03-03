<?php
    session_start();
    if(isset($SESSION['mysesh'])){
        header('location: page2.php');
    }elseif(isset($_COOKIE['cookie_name'])){
        header('location: page2.php');
    }


    if(isset($_POST['login'])){
        $username = $_POST['username'];
        $password = $_POST['password'];

        if($username == 'cc' && $password == 'se'){
            if(isset($_POST['remember'])){
                setcookie('cookie_name', 'ccse', time() + 1000000);
            }else{
                $_SESSION['mysesh'] = 'silorio';
            }
            header('location: page2.php');
        }else{
            echo "Invalid credentials!";
        }
    }
 ?>   
<!DOCTYPE html>
<html>
<body>

<h1>Medthod Page</h1>

<!-- <a href="page2.php?var=hello&var2=world&var3=hi"> Go to page 2</a>
-->
<form action="" method="POST">
    <input type="text" name="username" placeholder="Input your username">
    <input type="password" name="password" placeholder="Password">
    <input type="checkbox" name="remember"/>Remember me    
    <input type="submit" name="login" placeholder="Login">
</body>
</html>