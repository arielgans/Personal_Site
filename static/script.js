function displayPhone() {
  var x = document.getElementById("phoneNumber");
  if (x.style.visibility == "hidden") {
    x.style.visibility = "visible";
  } else {
    x.style.visibility = "hidden";
  }
} 
function displayEmail() {
  var x = document.getElementById("emailAddress");
  if (x.innerHTML === "") {
    x.innerHTML = "agans@uwaterloo.ca";
  } else {
    x.innerHTML = "";
  }
}

function copyPhone() {
  var copyText = "(+1) 416-953-4293";
  copyText.select();
  copyText.setSelectionRange(0, 99999);
  document.execCommand("copy");
  alert("Copied the text: " + copyText.value);
}
