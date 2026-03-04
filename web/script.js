document.addEventListener('DOMContentLoaded', function() {
    const priceElement = document.getElementById('latest-price');
    const buyButton = document.getElementById('buy-button');
    const sellButton = document.getElementById('sell-button');

    // Update price feed example
    function fetchPrice() {
        priceElement.textContent = '$1,850'; // Example static price; connect dynamically later
    }

    // Simulate buy action
    buyButton.addEventListener('click', function() {
        alert('Buy order placed (example action).');
    });

    // Simulate sell action
    sellButton.addEventListener('click', function() {
        alert('Sell order placed (example action).');
    });

    // Initial setup
    fetchPrice();
});