$(window).scroll(function () {
  if ($(window).width() > 767) {
    let x = $(window).scrollTop();
    if (x > 299) {
      $("#upper").css("display", "block");
    } else {
      $("#upper").css("display", "none");
    }
  }
});
