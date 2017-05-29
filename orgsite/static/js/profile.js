$(document).ready(function() {
	$(".btn-pref .btn").click(function () {
	    $(".btn-pref .btn").removeClass("btn-primary").addClass("btn-default");
	    // $(".tab").addClass("active"); // instead of this do the below 
	    $(this).removeClass("btn-default").addClass("btn-primary");   
	});

	$("#myBtn").click(function(){
        $("#myModal").modal();
    });

    $('.timeline-panel').click(function() {
	    $('.timeline-body', this).toggle(); // p00f
	});
});