<?php
if(isset($_FILES["file"]["type"])) {
    header('Content-type:application/json;charset=utf-8');

    $sourcePath = $_FILES['file']['tmp_name'];
    $targetPath = "decrypt_in.ppm";
    move_uploaded_file($sourcePath, $targetPath);

    $cmd = '/usr/bin/python3 decryptappm.py "decrypt_in.ppm"';
    $poruka = shell_exec($cmd);
    $uspjeh = true;
    echo json_encode(array(
        "uspjeh" => $uspjeh,
        "poruka" => $poruka,
    ));
}
