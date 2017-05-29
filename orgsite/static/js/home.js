function searchOrg() {
    var input, filter, ul, li, a, i, name;
    input = document.getElementById('search-input');
    filter = input.value.toUpperCase().replace(/[^A-Z0-9]/ig, "");
    ul = document.getElementById("org-list");
    li = ul.getElementsByTagName('li');

    for (i = 0; i < li.length; i++) {
        a = li[i].getElementsByTagName("a")[0];
        name = li[i].getElementsByTagName("input")[1];
        if (a.innerHTML.toUpperCase().replace(/[^A-Z0-9]/ig, "").indexOf(filter) > -1 || name.value.toUpperCase().replace(/[^A-Z0-9]/ig, "").indexOf(filter) > -1) {
            li[i].style.display = "";
        } else {
            li[i].style.display = "none";
        }
    }
}

function byCategory(category) {
    var ul, li, a, i;
    ul = document.getElementById("org-list");
    li = ul.getElementsByTagName('li');

    for (i = 0; i < li.length; i++) {
        a = li[i].getElementsByTagName("input")[0];
        if (a.value.toUpperCase() == category) {  
            li[i].style.display = "";
        } else {
            li[i].style.display = "none";
        }
    }
}

function showAll() {
    var ul, li, i;
    ul = document.getElementById("org-list");
    li = ul.getElementsByTagName('li');

    // Loop through all list items, and hide those who don't match the search query
    for (i = 0; i < li.length; i++) {
        li[i].style.display = "";
    }
}

  jQuery(document).ready(function($) {
 
        $('#myCarousel').carousel({
                interval: 5000
        });
 
        $('#carousel-text').html($('#slide-content-0').html());
 
        //Handles the carousel thumbnails
       $('[id^=carousel-selector-]').click( function(){
            var id = this.id.substr(this.id.lastIndexOf("-") + 1);
            var id = parseInt(id);
            $('#myCarousel').carousel(id);
        });
 
 
        // When the carousel slides, auto update the text
        $('#myCarousel').on('slid.bs.carousel', function (e) {
                 var id = $('.item.active').data('slide-number');
                $('#carousel-text').html($('#slide-content-'+id).html());
        });
});