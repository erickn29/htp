$(document).ready(function(){
    console.log($(document).width())
    if ($(document).width() < 591){
        console.log($(document).width())
        $('.left-menu').toggleClass('left-slider')
    }
})
