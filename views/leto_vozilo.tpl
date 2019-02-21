% rebase('osnova')
%if avti:
  <h1 class="title">
    Avtomobili letnika {{leto}} so:
  </h1>
  <p class="subtitle">
  <ol>
  % for znamka, model, oblika, letnik, barva, gorivo in avti:
    <li> {{znamka}} {{model}} {{oblika}} {{barva}} {{gorivo}} </li>
  % end
  </ol>
  </p>
%else:
<h1 class="title">
    V bazi ni podatkov za avtomobile letnika {{leto}}.
  </h1>
% end
