var totalprice = document.getElementById("totalprice");
function quantityfunc(q){
var price = q.parentElement.children[9].children[0].value;
q.parentElement.children[11].innerhtml = q.value * price;
}

