% rebase('osnova')

% if napaka:
<p>Prišlo je do napake!</p>
% end


<form method="post">
Številka šasije: <input type="text" name="stevilka_sasije" value="{{stevilka_sasije}}" /><br />
Letnik: <input type="text" name="letnik" value="{{letnik}}" /><br />
Oseba: <input type="text" name="oseba" value="{{oseba}}" /><br />
Model: <input type="text" name="model"  value="{{model}}" /><br />

Barva: <select name="barva">
% for id, barva in vse_barve:
    <option value="{{id}}" {{'selected' if str(id) in barva else ''}}>{{barva}}</option>
% end
</select>
<br />

Gorivo: <select name="gorivo">
% for id, gorivo in vsa_goriva:
    <option value="{{id}}" {{'selected' if str(id) in gorivo else ''}}>{{gorivo}}</option>
% end
</select>
<br />

Oblike: <select name="oblika">
% for id, oblika in vse_oblike:
    <option value="{{id}}" {{'selected' if str(id) in oblika else ''}}>{{oblika}}</option>
% end
</select>
<br />

<input type="submit" value="Dodaj film">
</form>