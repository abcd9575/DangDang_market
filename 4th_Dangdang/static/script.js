$(document).ready(function(){
    $(".list-group-action").click(function() {
        let title=$(this).attr('id')
        $.get("http://127.0.0.1:5000/detail")
    })
})