<?php
if(isset($_FILES["file"]["type"]) && isset($_POST['poruka'])) {
    $sourcePath = $_FILES['file']['tmp_name'];
    $targetPath = "encrypt_in.ppm";
    move_uploaded_file($sourcePath, $targetPath);

    $poruka = $_POST['poruka'];
    /*
    pozovi .py za kriptiranje i vrati uspjeh
    */
    $cmd = '/usr/bin/python3 encryptappm.py "encrypt_in.ppm" "encrypt_in_decrypted.ppm" "' . $poruka . '" 2>&1';
    $uspjeh = shell_exec($cmd);
    echo $uspjeh;
}
