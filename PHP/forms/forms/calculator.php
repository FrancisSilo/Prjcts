<?php
    if(isset($_POST['btn_calculate'])){
        $first_num = $_POST['first_num'];
        $operator = $_POST['operator'];
        $second_num = $_POST['second_num'];    
    }
    ?>

<!DOCTYPE html>
<html>
<link rel="stylesheet" href="styles.css">
<body>
<form action="" method="post">
    <input type="number" name="first_num" placeholder="Input first number"/><br><br>

    <select name="operator">
        <option value="+">+</option>
        <option value="-">-</option>
        <option value="*">*</option>
        <option value="/">/</option>
</select>
<br>
<br>
    <input type="number" name="second_num" placeholder="Input second number" /> <br><br>
    <input type="submit" name="btn_calculate" value="Calculate"/>
</form>
<?php
    if(isset($_POST['btn_calculate'])){

    echo "Result is: " . ' ' . $first_num . ' ' . $operator . ' ' . $second_num , '=';
    if ($operator === '+') {
        echo $first_num + $second_num;
    } elseif ($operator === '-') {
        echo $first_num - $second_num;
    } elseif ($operator === '*') {
        echo $first_num * $second_num;
    } elseif ($operator === '/') {
        if ($second_num != 0) {
            echo ($first_num / $second_num);
        } else {
            echo "Error: Division by zero!";
        }
    } else {
        echo "Invalid operator!";
    }
}
?>
</body>
</html>