<!DOCTYPE html>
<html>
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>Hello Bulma!</title>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/bulma/0.7.4/css/bulma.min.css">
    <script defer src="https://use.fontawesome.com/releases/v5.3.1/js/all.js"></script>
  </head>
  <body>
  <section class="section">
    <div class="container">
      <h1 class="title">
        Dobrodošli v bazi avtomobilov!
      </h1>
      <p class="subtitle">
        Na voljo vam je:
        %for leto in leta:
            <ol> 
            <a href= "/letniki-vozil/{{leto}}/">
            Avtomobili z letnico {{leto}}
            </a> 
            </ol>
        % end
      </p>
    </div>
  </section>
  </body>
</html>