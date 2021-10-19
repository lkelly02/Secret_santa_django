function deleteFunction() {
    var txt;
    var r = confirm("Are you sure you want to delete the checked Households?");
    if (r == true) {
        txt = "You pressed OK!";
    } else {
        txt = "You pressed Cancel!";
    }
    document.getElementById("delete_household").innerHTML = txt;
}