% rebase('osnova')
<h1 class="title">
  Izbirate lahko med:
</h1>
<p class="subtitle">
  
  %for leto in leta:
      <ol> 
      <a href= "/letniki-vozil/{{leto}}/">
      Avtomobili z letnico {{leto}}
      </a> 
      </ol>
  % end
</p>