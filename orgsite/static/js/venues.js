function searchVens() {
    var input, filter, ul, li, a, i, name;
    input = document.getElementById('search-input');
    filter = input.value.toUpperCase().replace(/[^A-Z0-9]/ig, "");
    ul = document.getElementById("ven-list");
    li = ul.getElementsByTagName('li');

    for (i = 0; i < li.length; i++) {
        a = li[i].getElementsByTagName("strong")[0]; 
        //name = li[i].getElementsByTagName("input")[1];
        if (a.innerHTML.toUpperCase().replace(/[^A-Z0-9]/ig, "").indexOf(filter) > -1) {
            li[i].style.display = ""; 
        } else {
            li[i].style.display = "none";
        }
    }
}