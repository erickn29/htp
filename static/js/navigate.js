$(document).ready(function(){
    let headerId = 'nav-id'
    let counter = 0
    let menu = $('.left-menu-sticky')
    let headers = $('.content').find('h2')
    headers.each(function(){
        $(this).attr('id', `${headerId}-${counter}`)
        counter = counter + 1
    })
    let list = []
    let add = function(){
        headers.each(function(){
            list.push(`<a href="#${$(this).attr('id')}">${$(this).html()}</a><br>`)
        })
    }
    add()
    menu.html(list)
})