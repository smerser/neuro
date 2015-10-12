 $(document).ready(function(){
    
    $("input#gem").prop('disabled', true);

    $("td").change(function(){
      $("input#gem").prop('disabled', false);
    });

  });
