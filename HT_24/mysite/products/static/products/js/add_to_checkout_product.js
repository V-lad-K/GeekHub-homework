$(document).ready(function() {
    $('.add_to_checkout_btn').click(function(e) {
        e.preventDefault()

        let productId = $(this).data('productid')
        let quantityInput = document.getElementById("quantity_" + productId)
        let csrftoken = $("[name=csrfmiddlewaretoken]").val()
        let dataToSend = {
            currentPage: "products"
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
