$(document).ready(function(){
    let headerId = 'nav-id'
    let counter = 0
    let menu = $('.menu-toggle')
    let headers = $('.content').find('h2')
    headers.each(function(){
        $(this).attr('id', `${headerId}-${counter}`)
        counter = counter + 1
    })
    let list = []
    let add = function(){
        headers.each(function(){
            list.push(`<div class="right-link"><a href="#${$(this).attr('id')}">${$(this).html()}</a></div>`)
        })
    }
    add()
    menu.html(list)
})