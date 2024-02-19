function hideContainerProduct(tagSelectorClass){
    let containerTag = document.querySelector(tagSelectorClass)
    containerTag.style.display = "none"
}


$(document).ready(function() {
    $('.delete_product_btn').click(function(e) {
        e.preventDefault()

        let productId = $(this).data('productid')
        let csrftoken = $("[name=csrfmiddlewaretoken]").val()
        let containerClassName = ".container_product_" + productId

        $.ajax({
            url: '/api/checkout/' + productId + "/",
            method: 'DELETE',
            headers: {
                'X-CSRFToken': csrftoken
            },
            success: function(response) {
                hideContainerProduct(containerClassName)
            },
            error: function(response) {
                console.error('Error:', response)
            }
        })
    })
})
