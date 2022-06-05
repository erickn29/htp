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

$('#them-toggler').click(function(){
    if ($('#css-theme').attr('href') == "static/css/dark.css"){
        $('#css-theme').attr("href", "static/css/white.css")
        $('#code-theme').attr("href", "static/css/hljs/default.min.css")

    }else{
        $('#css-theme').attr("href", "static/css/dark.css")
        $('#code-theme').attr("href", "static/css/hljs/onedark.min.css")
    }
    
})