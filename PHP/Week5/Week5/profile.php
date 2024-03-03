<?php include("connection.php"); ?>

<?php
    if(isset($_GET['id'])){
        $id = $_GET['id'];

        $sql = "SELECT * FROM tblstudents WHERE id = $id";
        $result = mysqli_query($conn, $sql);

        if (mysqli_num_rows($result) > 0){
            while($row = mysqli_fetch_assoc($result)){
                $studentid = $row['id'];
                $fullname = $row['first_name'] . " " . $row['middle_name'] . " " . $row['last_name'];
                $firstname = $row['first_name'];
                $middlename = $row['middle_name'];
                $lastname = $row['last_name'];
                $course = $row['course'];
            } 
        } else {
            echo "<h3>No records found!</h3>";
        }
    }else{
        die(mysqli_connect_error());
    }
?>
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, intial-scale=1.0">
    <title>Profile</title>
</head>
<body>
        <p>Welcome <strong><?php echo $fullname;?>!</strong></p>
        <p>First Name: <strong><?php echo $firstname;?></strong></p>
        <p>Middle Name: <strong><?php echo $middlename;?></strong></p>
        <p>Last Name: <strong><?php echo $lastname;?></strong></p>
        <p>Course: <strong><?php echo $course;?></strong></p>
        
</body>
</html>      