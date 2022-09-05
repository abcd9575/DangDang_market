$(document).ready(function() {
    $(".btn-list").click(function() {
        let title = $(this).attr('id');
        $.get("/detail?title=" + title)
            .then(function(result){
                $("#exampleModalLabel").text(result.title);
                $(".modal-body").html(result.content);
                $(".modal").modal('show');
        });
    });
});