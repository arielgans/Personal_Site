$(function () {
  $('[data-toggle="popover"]').popover()
})

function copyPhone() {
  var copyText = "(+1) 416-953-4293";
  copyText.select();
  copyText.setSelectionRange(0, 99999);
  document.execCommand("copy");
  alert("Copied the text: " + copyText.value);
}
