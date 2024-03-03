<?php
    session_start();
?>
<!DOCTYPE html>
<html>
<body>

<h1>This is page 3</h1>

<?php
    echo $_SESSION['mysesh'];
?>
</body>
</html>