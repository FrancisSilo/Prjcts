<?php include("connection.php"); ?>

<?php
    if(isset($_POST['submit_btn'])){

        $firstname = $_POST['txtfname'];
        $middlename = $_POST['txtmname'];
        $lastname = $_POST['txtlname'];
        $position = $_POST['position'];

        $insert = mysqli_query($conn, 
                "INSERT INTO employees (first_name, middle_name, last_name, position)
                VALUES('$firstname', '$middlename', '$lastname', '$position')");
        
        if(!$insert){
                die(mysqli_error($insert));
        }else{
            header("location: employees.php");
        }
    }
?>

<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Add New Employee</title>
</head>
<body>
    <h1>Add User</h1>
    <form method="POST" action="<?php echo $_SERVER['PHP_SELF'];?>">
        <div><input type="text" name="txtfname" placeholder="First Name"/></div>
        <div><input type="text" name="txtmname" placeholder="Middle Name"/></div>
        <div><input type="text" name="txtlname" placeholder="Last Name"/></div>
        <div><input type="date" name="birthdate" placeholder="Birthdate"/></div>
        <p>Position: </p>
        <select name="position" id="position">
            <option value="Agent"> Agent </option>
            <option value="Manager"> Manager </option>
            <option value="Admin"> Admin </option>
        </select>    
        <div><input type="submit" name="submit_btn" placeholder="Save"/></div>
    </form>

  </body>
</html>

<?php mysqli_close($conn); ?>
