% rebase('osnova')
<h1 class="title">
  Avtomobili znamke {{niz}} so:
    </h1>
    <p class="subtitle">
    <ol>
    % for model, oblika, letnik, barva, gorivo in avtomobili_znamk:
    <li>  {{oblika}} {{letnik}} {{barva}} {{gorivo}} </li>
    % end
    </ol>
    </p>