<?php
    // Set MySQL connection parameters
    $servername = "localhost:3306";
    $username = "root";
    $password = "";
    $dbname = "company";

    // Create connection
    $conn = mysqli_connect($servername, $username, $password, $dbname);

    // Check connection
    if (!$conn) {
        die("Connection failed: " . mysqli_connect_error());
    } else {
    }
?>
