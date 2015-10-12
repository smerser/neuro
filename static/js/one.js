
$(document).ready(function(){

  $("label[for=id_dr").text('Læge');
          
  $("input#gem").prop('disabled', true);

  $("td").change(function(){
     $("input#gem").prop('disabled', false);
  });
          
  $("input#add").click(function(){
     window.location='/add/'
  });

  $("input#flyt").click(function(){
     $("input#id_seneste").val($("input#id_booking").val());
  });

  $("input#cpr").click(function(){
     window.location='/neuro/cpr/' + $("input.cpr").val();
  });

  $("input.cpr").keypress(function(e){
    var keycode = (e.keyCode ? e.keyCode: e.which);
    if(e.which == 13)
      window.location='/neuro/cpr/' + $("input.cpr").val();
  });


  var picker = new Pikaday({
     field: $("input#id_start")[0],
     onOpen: function() { $("input#id_start").val(this.getMoment().format('YYYY-MM-DD')); }
  });

  var picker = new Pikaday({
     field: $("input#id_seneste")[0],
     onOpen: function() { $("input#id_seneste").val(this.getMoment().format('YYYY-MM-DD')); }
  });

  var picker = new Pikaday({
     field: $("input#id_booking")[0],
     onOpen: function() { $("input#id_booking").val(this.getMoment().format('YYYY-MM-DD')); }
  });

});
