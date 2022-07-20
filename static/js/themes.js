$('#theme-toggler').click(function(){
    if ($('#css-theme').attr('href') == "static/css/dark.css"){
        $('#css-theme').attr("href", "static/css/white.css")
        $('#code-theme').attr("href", "static/css/hljs/default.min.css")
        $('#map').attr("src", "/static/img/map-white.png")
        $('#like').attr("src", "/static/img/social-white.png")
        $('#up').attr("src", "/static/img/angle-up-white.png")
        $('#burger').attr("src", "/static/img/menu-burger-white.png")
        $('#theme-toggler').attr("src", "/static/img/moon.png")
        let theme = $('#css-theme').attr('href')
        $.ajax(
            {
                url: "/set_cookie",
                data: {'theme': theme},
                success: function(result){
                $("#l-content").html(result);
                }
            }
        );

    }else{
        $('#css-theme').attr("href", "static/css/dark.css")
        $('#code-theme').attr("href", "static/css/hljs/onedark.min.css")
        $('#map').attr("src", "/static/img/map-dark.png")
        $('#like').attr("src", "/static/img/social-dark.png")
        $('#up').attr("src", "/static/img/angle-up-dark.png")
        $('#burger').attr("src", "/static/img/menu-burger-dark.png")
        $('#theme-toggler').attr("src", "/static/img/sun.png")
        let theme = $('#css-theme').attr('href')
        $.ajax(
            {
                url: "/set_cookie",
                data: {'theme': theme},
                success: function(result){
                $("#l-content").html(result);
                }
            }
        );
    }
    
})
