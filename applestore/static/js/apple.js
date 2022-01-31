$(document).ready(function() {
    $(document).on('click', '#submit', function(e){
        e.preventDefault();
        value = $("#product_id").val()
        console.log(value)
        $.ajax({
            type: 'GET',
            url: '/apple/get_product/'+value,
            success: function(response) {
                $("#api_res").text(response)
            },
            error: function(response) {
                $("#api_res").text("Error, Please enter Valid ID")
            },
        });
    })
})