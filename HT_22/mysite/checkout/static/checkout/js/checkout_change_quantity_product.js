$(document).ready(function() {
    $('.change_quantity_product_btn').click(function(e) {
        e.preventDefault()

        let productId = $(this).data('productid')
        let quantityInput = document.getElementById("quantity_" + productId)
        let csrftoken = $("[name=csrfmiddlewaretoken]").val()

        let dataToSend = {
            currentPage: "checkout"
        }

        $.ajax({
            url: '/api/checkout/' + productId + "/" + quantityInput.value + "/",
            method: 'PUT',
            headers: {
                'X-CSRFToken': csrftoken
            },
            data: dataToSend,
            error: function(response) {
                console.error('Error:', response)
            }
        })
    })
})