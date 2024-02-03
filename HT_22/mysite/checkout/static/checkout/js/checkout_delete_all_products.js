function hideContainerProduct(tagSelectorClass){
    let containerTag = document.querySelector(tagSelectorClass)
    containerTag.style.display = "none"
}


$(document).ready(function() {
    $('.delete_all_products_btn').click(function(e) {
        e.preventDefault()

        let csrftoken = $("[name=csrfmiddlewaretoken]").val()
        let containerClassName = ".order_products"

        $.ajax({
            url: '/api/checkout/delete_all/',
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
