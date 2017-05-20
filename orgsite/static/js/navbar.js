$(document).ready(function(){
	$(window).on("scroll",function(){
  	var wn = $(window).scrollTop();
    if(wn > 50){
    	$(".navbar").css("background","rgba(255, 255, 255)");
    }
    else{
    	$(".navbar").css("background","rgba(0,0,0,0)");
    }
  });

  // $('#main-navbar').on('show.bs.collapse', function () {
  //   $(".collapse").css("background-color","rgba(255, 255, 255)");
  //   $(".navbar").css("background","rgba(255, 255, 255)");
  //   $(".navbar").css("border-color","rgba(255, 255, 255)");
  // });

  // $('#main-navbar').on('shown.bs.collapse', function () {
  //   $(".navbar").css("background-color","rgba(255, 255, 255)");
  //   $(".collapse").css("background","rgba(255, 255, 255)");
  //   $(".collape").css("border-color","rgba(255, 255, 255)");

  // });

  // $('#main-navbar').on('hide.bs.collapse', function () {
  //    $(".collapse").css("background","rgba(255, 255, 255)");
  //   $(".collapse").css("background-color","rgba(255, 255, 255)");
  //   $(".collape").css("border-color","rgba(255, 255, 255)");
  // });

  // $('#main-navbar').on('hidden.bs.collapse', function () {
  //   $(".collapse").css("background-color","rgba(0,0,0,0)");
  //   $(".collape").css("border-color","rgba(0,0,0,0)");
    
  // });

});