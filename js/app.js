$(document).foundation();

$(window).scroll(function() {
  $("#badge-acreditacion").css("opacity", 1 - $(window).scrollTop() / 250);
});

 const lenis = new Lenis()
    lenis.on('scroll', (e) => {
      console.log(e)
    })
    function raf(time) {
      lenis.raf(time)
      requestAnimationFrame(raf)
    }
    requestAnimationFrame(raf)