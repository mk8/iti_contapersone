<?php
  $stato = file_get_contents ("stato.txt");
  $ir1 = file_get_contents ("ir1.txt");
  $ir2 = file_get_contents ("ir2.txt");
  $nPersone = file_get_contents ("numero_persone.txt");
?>
<!doctype html>
<html>
  <head>
    <title>ContaPersone</title>
  </head>
  <body>
    <p>Stato: <strong><?= $stato ?></strong></p>
    <p>Ir1: <strong><?= $ir1 ?></strong></p>
    <p>Ir2: <strong><?= $ir2 ?></strong></p>
    <p>Numero Persone: <strong><?= $nPersone ?></strong></p>
  </body>
</html>
