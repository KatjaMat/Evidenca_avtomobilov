<!DOCTYPE html>
<html>
  <head>
  % rebase('osnova')
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>Hello Bulma!</title>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/bulma/0.7.4/css/bulma.min.css">
    <script defer src="https://use.fontawesome.com/releases/v5.3.1/js/all.js"></script>
  </head>
  <body>
  <section class="section">
    <div class="container">
    %if avti:
      <h1 class="title">
        Avtomobili letnika {{leto}} so:
      </h1>
      <p class="subtitle">
      <ol>
      % for a, leto, barva, gorivo, oseba, model in avti:
        <li>{{model}} {{leto}} {{barva}} {{gorivo}} </li>
      % end
      </ol>
      </p>
    %else:
    <h1 class="title">
        V bazi ni podatkov za avtomobile letnika {{leto}}.
      </h1>
    % end
    </div>
  </section>
  </body>
</html>