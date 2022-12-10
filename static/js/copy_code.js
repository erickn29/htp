let addHtml = `<div class="copy_text"><button type="button" class="btn btn-outline-secondary">copy</button></div>`

let copyText = function(){
    $('.copy_text').on('click', function(){
        let txt = $(this).prev()
        navigator.clipboard.writeText(txt.text());
        let thisBtn = $(this).children(".btn")
        thisBtn.text('copied!')
        thisBtn.removeClass("btn-outline-secondary")
        thisBtn.addClass("btn-outline-success")

        // setTimeout(function(){
        //     thisBtn.text('copy')
        //     thisBtn.removeClass("btn-outline-success")
        //     thisBtn.addClass("btn-outline-secondary")
        // }, 1000);
    })
}

$(document).ready(function(){
    $('pre').append(addHtml)
    copyText()
})
