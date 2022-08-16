$(document).ready(function() {
    $(".btn-list").click(function() {
        let title = $(this).attr('id');
        $.get("http://127.0.0.1:5000/detail?title=" + title)
            .then(function(result){
                $("#exampleModalLabel").text(result.title);
                $(".modal-body").text(result.content);
                $(".modal").modal('show');
        });
        
    });
});