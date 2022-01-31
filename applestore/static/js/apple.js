$(document).ready(function() {
    $(document).on('click', '#submit', function(e){
        e.preventDefault();
        console.log("clicked")
        value = $("#product_id").val()
        console.log(value)
        $.ajax({
            type: 'GET',
            url: '/apple/get_product/'+value,
            success: function(response) {
                console.log(response)
            }
        });
    })
})