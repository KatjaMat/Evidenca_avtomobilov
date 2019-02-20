% rebase('osnova')
<h1 class="title">
  Izbirate lahko med:
</h1>
<p class="subtitle">
  %for znamka in znamke:
      <ol> 
      <a href= "/znamke-vozil/{{znamka}}/">
      {{znamka}}
      </a> 
      </ol>
  % end
</p>
