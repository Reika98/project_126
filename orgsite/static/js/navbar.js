$(document).ready(function(){
	$(window).on("scroll",function(){
  	var wn = $(window).scrollTop();
    if(wn > 50){
    	$(".navbar").css("background","rgba(21, 67, 96)");
      $(".navbar").css("box-shadow","5px 0px 10px 1px black");
    }
    else{
    	$(".navbar").css("background","rgba(0,0,0,0)");
      $(".navbar").css("box-shadow", "0 0 0px transparent");
    }
  });

});