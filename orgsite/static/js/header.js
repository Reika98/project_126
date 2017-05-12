$(document).ready(function(){
	window.addEventListener("scroll", function () {
			onscroll();
	}, false);

  
});

function onscroll(){
  	var scroll = $(window).scrollTop();
	  if (scroll > 50) {
	    $(".navbar").css("background-color" , "white");
	  }
	  else{
		  $(".navbar").css("background-color" , "transparent");  	
	  }
  }