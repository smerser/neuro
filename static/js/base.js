$(document).ready(function(){

// GO TO CLICKED ID
    $("tr").click(function(){
	//var id = $(this).find('input[type="hidden"]');
	location.href = "/one/" + $(this).attr('id');
    });

// GO TO LOGOUT
    $("input#logout").click(function(){
      window.location='neuro/logout/';
    });

// IMPUT MASK
    $("input#id_cpr").mask("999999-9999");
    $("input#txt").mask("999999-9999");

 });
