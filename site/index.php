<html>
  <head>
    <title>PHP Test</title>
  </head>
  <body>
    <p>Before:</p>
    <?php
      echo shell_exec('/usr/bin/python3 encryptappm.py "lenna.ppm" "out.ppm" "Finalno cini se da sve lepo radi i to je to" 2>&1');
      echo shell_exec('/usr/bin/python3 decryptappm.py "out.ppm"');
    ?>
  </body>
</html>
