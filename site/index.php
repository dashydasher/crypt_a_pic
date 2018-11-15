<html>
  <head>
    <title>PHP Test</title>
  </head>
  <body>
    <?php
      echo shell_exec('/usr/bin/python3 encryptappm.py "encrypt_in.ppm" "encrypt_in_decrypted.ppm" "Ja sam danas dosta dobar" 2>&1');
      echo shell_exec('/usr/bin/python3 decryptappm.py "decrypt_in.ppm"');
    ?>
  </body>
</html>
