function pop(){
    if ($('.left-slider').css('left') == '-300px'){
        $('.left-slider').css('left', '0px')
        $('body').css('overflow', 'hidden')
        $('.cover').css('display', 'block')
    } else {
        $('.left-slider').css('left', '-300px')
        $('body').css('overflow', 'auto')
        $('.cover').css('display', 'none')
    }
    
}
