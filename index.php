<?php
require_once 'vendor/autoload.php';
use Models\Helper;

ob_start("Models\Helper::sanitize_output");

$loader = new Twig_Loader_Filesystem('public/views');
$twig = new Twig_Environment($loader);

$data = include('config/app.php');

echo $twig->render('index.html.twig', array(
    "app" => $data,
));
