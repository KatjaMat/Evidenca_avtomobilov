% rebase('osnova')
%if avti:
  <h1 class="title">
    Avtomobili letnika {{leto}} so:
  </h1>
  <table class="table">
    <thead>
    <tr>
      <th>znamka</th>
      <th>model</th>
      <th>oblika</th>
      <th>barva</th>
      <th>gorivo</th>
      <th>oseba</th>
    </tr>
    </thead>
  <p class="subtitle">
  % for podatki in avti:
  <tr>
      <td>{{podatki[0]}}</td>
      <td>{{podatki[1]}}</td>
      <td>{{podatki[2]}}</td>
      <td>{{podatki[4]}}</td>
      <td>{{podatki[5]}}</td>
      <td><a href="/letniki-vozil/{{leto}}/{{podatki[6]}}/">{{podatki[6]}}</a></td>
  </tr>
  % end
  </table>
  </p>
%else:
<h1 class="title">
    V bazi ni podatkov za avtomobile letnika {{leto}}.
  </h1>
% end
