% rebase('osnova')
<h1 class="title">
  Avtomobili znamke {{niz}} so:
    </h1>

    <body>
    <table class="table">
    <thead>
    <tr>
      <th>oblika</th>
      <th>letnik</th>
      <th>barva</th>
      <th>gorivo</th>
    </tr>
    </thead>
      % for podatki  in avtomobili_znamk:
      <tr>
      <td>{{podatki[1]}}</td>
      <td>{{podatki[2]}}</td>
      <td>{{podatki[3]}}</td>
      <td>{{podatki[4]}}</td>
      </tr>
      % end
    </table>
    </p>
    <body/>
