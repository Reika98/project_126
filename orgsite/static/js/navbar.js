$(document).ready(function(){
	$(window).on("scroll",function(){
  	var wn = $(window).scrollTop();
    if(wn > 50){
    	$(".navbar").css("background","rgba(255, 255, 255)");
      $(".navbar").css("padding-top","0px");
    }
    else{
    	$(".navbar").css("background","rgba(0,0,0,0)");
       $(".navbar").css("padding-top","10px");
    }
  });

  $('#main-navbar').on('show.bs.collapse', function () {
    $(".collapse").css("background-color","rgba(255, 255, 255)");

  });
  $('#main-navbar').on('shown.bs.collapse', function () {
    $(".nav").css("background-color","rgba(255, 255, 255)");
    $(".navbar-collapse").css("background-color","rgba(255, 255, 255)");


  });

  $('#main-navbar').on('hide.bs.collapse', function () {
    $(".collapse").css("background-color","rgba(0,0,0,0)");
    
  });
  $('#main-navbar').on('hidden.bs.collapse', function () {
    $(".collapse").css("background-color","rgba(0,0,0,0)");
    
  });

});