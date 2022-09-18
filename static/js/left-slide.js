$(document).ready(function(){
    if ($(document).width() < 591){
        let slide_menu = $('.right-menu-sticky')
        slide_menu.addClass('left-slider')
        slide_menu.removeClass('right-menu-sticky')
    }
})
