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
    </tr>
    </thead>
  <p class="subtitle">
  % for znamka, model, oblika, letnik, barva, gorivo in avti:
  <tr>
      <td>{{znamka}}</td>
      <td>{{model}}</td>
      <td>{{oblika}}</td>
      <td>{{barva}}</td>
      <td>{{gorivo}}</td>
  </tr>
  </table>
  % end
  </p>
%else:
<h1 class="title">
    V bazi ni podatkov za avtomobile letnika {{leto}}.
  </h1>
% end
