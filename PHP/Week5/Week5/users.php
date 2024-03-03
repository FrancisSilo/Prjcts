<?php include("connection.php")
?>
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, intial-scale=1.0">
    <title>All Users</title>
<style>
    table, th, td{
        border: 1px solid black;
        border-collapse: collapse;
        padding: 20px;
    }
    th {
        background-color: #607274;
    }
</style>

</head>
<body>
    <table>
        <table border="1">
            <thead>
                <tr>
                <table style=width:100%>
                    <th>ID</th>
                    <th>First Name</th>
                    <th>Middle Name</th>
                    <th>Last Name</th>
                    <th>Course</th>
                    <th>Link</th>
                </tr>
            </thead>
            <tbody>
    <?php
        $sql = "SELECT * FROM tblstudents";
        $result = mysqli_query($conn, $sql);

        if (mysqli_num_rows($result) > 0) {
            while($row = mysqli_fetch_assoc($result)){
    ?>
    <tr>
                <th><?php echo $row["id"];?></th>
                <td><?php echo $row["first_name"];?></td>
                <td><?php echo $row["middle_name"];?></td>
                <td><?php echo $row["last_name"];?></td>
                <td><?php echo $row["course"];?></td>
                <td><a href="profile.php?id=<?php echo $row["id"];?>">View Student</a></td>
    </tr>
    <?php        
            }
        }
    ?>
    </tbody>
    </table>
</body>
</html>
<?php mysqli_close($conn);?>