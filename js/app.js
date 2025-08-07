$(document).foundation();

$(window).scroll(function() {
  $("#badge-acreditacion").css("opacity", 1 - $(window).scrollTop() / 250);
});