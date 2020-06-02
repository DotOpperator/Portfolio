<?php
    if(isset($_POST['submit'])){
        $name = $_POST['name'];
        $visitor_email = $_POST['email'];
        $message = $_POST['message'];
    }

    $email_from = 'manoharchitoda@gmail.com';

    $email_subject = "New Form Submission";


    $to = "manoharchitoda@gmail.com";
    $headers = "From: ".$email_from;
    $txt = "You receieved an e-mail from ".$name.".\n\n".$message;
    mail($to,$email_subject,$txt,$headers);
    header("Location: index.html");

?>