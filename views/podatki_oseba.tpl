% rebase('osnova')

<p class="subtitle"> Podatki o lastniku vozila: </p>

<table class="table">
    <thead>
    <tr>
      <th>ime</th>
      <th>priimek</th>
      <th>naslov</th>
      <th>telefon</th>
    </tr>
    </thead>
% for podatek in podatki:
<td>{{podatek}}</td>
% end
</table>

