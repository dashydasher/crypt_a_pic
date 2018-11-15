<html>
  <head>
    <title>PHP Test</title>
  </head>
  <body>
    <?php
      echo shell_exec('/usr/bin/python3 encryptappm.py "lenna.ppm" "out.ppm" "Ja sam danas dosta dobar" 2>&1');
      echo shell_exec('/usr/bin/python3 decryptappm.py "out.ppm"');
    ?>
  </body>
</html>
