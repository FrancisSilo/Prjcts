<?php
include("connection.php");
?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>All Users</title>
    <style>
        table, th, td {
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
                    <th>ID</th>
                    <th>Full Name</th>
                    <th>Position</th>
                    <th>Salary</th>
                    <th>Action</th>
                </tr>
            </thead>
            <tbody>
                <?php
                $sql = "SELECT * FROM employees";
                $result = mysqli_query($conn, $sql);

                if (mysqli_num_rows($result) > 0) {
                    while ($row = mysqli_fetch_assoc($result)) {
                        ?>
                        <tr>
                            <th><?php echo $row["emp_id"]; ?></th>
                            <td><?php echo $row['first_name'] . " " . $row['middle_name'] . " " . $row['last_name']; ?></td>
                            <td><?php echo $row["position"]; ?></td>
                            <td>
                                <?php
                                switch ($row["position"]) {
                                    case "Agent":
                                        echo "$10,000";
                                        break;
                                    case "Manager":
                                        echo "$18,000";
                                        break;
                                    case "Admin":
                                        echo "$25,000";
                                        break;
                                    default:
                                        echo "N/A";
                                }
                                ?>
                            </td>
                            <td><a href="view.php?emp_id=<?php echo $row["emp_id"]; ?>">View Employee</a></td>
                        </tr>
                        <?php
                    }
                }
                ?>
            </tbody>
        </table>
    </body>
</html>

<?php
mysqli_close($conn);
?>
