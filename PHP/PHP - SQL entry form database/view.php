<?php
include("connection.php");

if (isset($_GET['emp_id'])) {
    $id = $_GET['emp_id'];

    $sql = "SELECT * FROM employees WHERE emp_id = $id";
    $result = mysqli_query($conn, $sql);

    if (mysqli_num_rows($result) > 0) {
        while ($row = mysqli_fetch_assoc($result)) {
            $id = $row['emp_id'];
            $fullname = $row['first_name'] . " " . $row['middle_name'] . " " . $row['last_name'];
            $position = $row['position'];
            $birthdate = $row['birthdate'];
            
            switch ($position) {
                case "Agent":
                    $salary = "$10,000";
                    break;
                case "Manager":
                    $salary = "$18,000";
                    break;
                case "Admin":
                    $salary = "$25,000";
                    break;
                default:
                    $salary = "N/A";
            }
        }
    } else {
        echo "<h3>No records found!</h3>";
    }
} else {
    die(mysqli_connect_error());
}
?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Profile</title>
</head>
<body>
    <p>Full Name: <strong><?php echo $fullname; ?></strong></p>
    <p>Position: <strong><?php echo $position; ?></strong></p>
    <p>Salary: <strong><?php echo $salary; ?></strong></p>
</body>
</html>

<?php
mysqli_close($conn);
?>
