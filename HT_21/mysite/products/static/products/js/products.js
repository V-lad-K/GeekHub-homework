function decreaseQuantity(tagId) {
    let quantityInput = document.getElementById(tagId);
    let currentQuantity = parseInt(quantityInput.value, 10);
    if (currentQuantity > 1) {
        quantityInput.value = currentQuantity - 1;
    }
}

function increaseQuantity(tagId) {
    let quantityInput = document.getElementById(tagId);
    let currentQuantity = parseInt(quantityInput.value, 10);
    quantityInput.value = currentQuantity + 1;
}
