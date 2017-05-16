function searchOrg() {
    var input, filter, ul, li, a, i;
    input = document.getElementById('search-input');
    filter = input.value.toUpperCase();
    ul = document.getElementById("org-list");
    li = ul.getElementsByTagName('li');

    for (i = 0; i < li.length; i++) {
        a = li[i].getElementsByTagName("a")[0];
        if (a.innerHTML.toUpperCase().indexOf(filter) > -1) {
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