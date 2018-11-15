<?php
namespace Models;

class Helper {

    /*
    služi za dohvaćanje korisnikovog inputa koji vjerojatno nije siguran
    */
    static function xssafe($data, $encoding='UTF-8') {
       return htmlspecialchars($data, ENT_QUOTES | ENT_HTML401, $encoding);
    }

    /*
    source kod pretvara u minimalni oblik bez uvlačenja
    */
    static function sanitize_output($buffer) {
        $search = array(
            '/\>[^\S ]+/s', //strip whitespaces after tags, except space
            '/[^\S ]+\</s', //strip whitespaces before tags, except space
            '/(\s)+/s'  // shorten multiple whitespace sequences
            );
        $replace = array(
            '>',
            '<',
            '\\1'
            );
      $buffer = preg_replace($search, $replace, $buffer);
        return $buffer;
    }

    static function startsWith($haystack, $needle) {
         $length = strlen($needle);
         return (substr($haystack, 0, $length) === $needle);
    }

    static function endsWith($haystack, $needle) {
        $length = strlen($needle);
        if ($length == 0) {
            return true;
        }

        return (substr($haystack, -$length) === $needle);
    }

    static function decryptID($ciphertext) {
        if(strlen($ciphertext) == 88) {
            $app_data = include('config/app.php');
            $key = $app_data->key;
            $c = base64_decode($ciphertext);
            $ivlen = openssl_cipher_iv_length($cipher="AES-128-CBC");
            $iv = substr($c, 0, $ivlen);
            $hmac = substr($c, $ivlen, $sha2len=32);
            $ciphertext_raw = substr($c, $ivlen+$sha2len);
            $id = openssl_decrypt($ciphertext_raw, $cipher, $key, $options=OPENSSL_RAW_DATA, $iv);
            $calcmac = hash_hmac('sha256', $ciphertext_raw, $key, $as_binary=true);
            if (hash_equals($hmac, $calcmac)) {
                return $id;
            }
        }
        return "";
    }

    static function encryptID($id) {
        $app_data = include('config/app.php');
        $key = $app_data->key;
        $plaintext = $id;
        $ivlen = openssl_cipher_iv_length($cipher="AES-128-CBC");
        $iv = openssl_random_pseudo_bytes($ivlen);
        $ciphertext_raw = openssl_encrypt($plaintext, $cipher, $key, $options=OPENSSL_RAW_DATA, $iv);
        $hmac = hash_hmac('sha256', $ciphertext_raw, $key, $as_binary=true);
        $ciphertext = base64_encode( $iv.$hmac.$ciphertext_raw );
        return $ciphertext;
    }

}
