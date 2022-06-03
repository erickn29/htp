function pop(){
    if ($('.left-content').css('left') == '-300px'){
        $('.left-content').css('left', '0px')
        $('body').css('overflow', 'hidden')
        $('.cover').css('display', 'block')
    } else {
        $('.left-content').css('left', '-300px')
        $('body').css('overflow', 'auto')
        $('.cover').css('display', 'none')
    }
    
}