% rebase('osnova')

% if napaka:
<p>Prišlo je do napake!</p>
% end

<p class="subtitle">Tukaj lahko dodate novo vozilo v bazo:</p>

<form method="post">
Številka šasije: <input type="integer" name="stevilka_sasije" value="{{stevilka_sasije}}" /><br />
Znamka: <input type="text" name="znamka" value="{{znamka}}" /><br />
Letnik: <input type="integer" name="letnik" value="{{letnik}}" /><br />
Oseba: <input type="text" name="oseba" value="{{oseba}}" /><br />
Model: <input type="text" name="model"  value="{{model}}" /><br />

Barva: <select name="barva">
% for barva in vse_barve:
    <option value="{{barva[0]}}" {{'selected' if str(vse_barve[0]) in barva else ''}}>{{barva[0]}}</option>
% end
</select>
<br />

Gorivo: <select name="gorivo">
% for gorivo in vsa_goriva:
    <option value="{{gorivo[0]}}" {{'selected' if str(vsa_goriva[0]) in gorivo else ''}}>{{gorivo[0]}}</option>
% end
</select>
<br />

Oblike: <select name="oblika">
% for oblika in vse_oblike:
    <option value="{{oblika[0]}}" {{'selected' if str(oblika[0]) in oblika else ''}}>{{oblika[0]}}</option>
% end
</select>
<br />

<input type="submit" value="Dodaj vozilo">
</form>