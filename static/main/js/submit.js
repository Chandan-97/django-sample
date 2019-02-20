$("#btn").on("click", function (event) {
    event.preventDefault();
    $name = $("#name").val().trim();
    console.log($name);
    $.ajax({
        type: "POST",
        url:  "/",
        data:{
            csrfmiddlewaretoken : $("input[name=csrfmiddlewaretoken").val(),
            "name" : $name,
        },
        success: function(data){
            $("#output").val(data);
            console.log(data);
        },
    });
});