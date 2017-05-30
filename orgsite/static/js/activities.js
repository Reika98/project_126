// $(document).ready(function() {
//     $('#pinBoot').pinterest_grid({
//         no_columns: 4,
//         padding_x: 10,
//         padding_y: 10,
//         margin_bottom: 50,
//         single_column_breakpoint: 700
//     });
// });

function searchActs() {
    var input, filter, ul, li, a, i, name;
    input = document.getElementById('search-input');
    filter = input.value.toUpperCase().replace(/[^A-Z0-9]/ig, "");
    ul = document.getElementById("act-list");
    li = ul.getElementsByTagName('li');

    for (i = 0; i < li.length; i++) {
        a = li[i].getElementsByTagName("h2")[0];
        //name = li[i].getElementsByTagName("input")[1];
        if (a.innerHTML.toUpperCase().replace(/[^A-Z0-9]/ig, "").indexOf(filter) > -1) {
            li[i].style.display = "";
        } else {
            li[i].style.display = "none";
        }
    }
}