/*jshint esversion: 6 */ // Specifies that we're using ES6 syntax

// Retrieve the Stripe public key from the HTML, removing the first and last characters
var stripePublicKey = $('#id_stripe_public_key').text().slice(1, -1);

// Retrieve the client secret from the HTML, removing the first and last characters
var clientSecret = $('#id_client_secret').text().slice(1, -1);

// Initialize a Stripe object with the public key
var stripe = Stripe(stripePublicKey);

// Create an instance of Elements, which manages all of your UI elements
var elements = stripe.elements();

// Define styles for the Stripe card element
var style = {
    base: {
        color: '#111',
        fontFamily: '"Roboto", sans-serif',
        fontSmoothing: 'antialiased',
        fontSize: '18px',
        '::placeholder': {
            color: '#abb8d5'
        }
    },
    invalid: {
        color: '#ed4656',
        iconColor: '#ed4656'
    }
};

// Create a card object and apply the style to it
var card = elements.create('card', { style: style });

// Mount the card element to the div with id 'card-element'
card.mount('#card-element');

// Handle real-time validation errors on the card element
card.addEventListener('change', function (event) {
    var errorDiv = document.getElementById('card-errors');
    if (event.error) {
        var html = `
            <span class="icon" role="alert">
                <i class="fas fa-times"></i>
            </span>
            <span>${event.error.message}</span>
        `;
        $(errorDiv).html(html);
    } else {
        errorDiv.textContent = '';
    }
});

// Handle form submission
var form = document.getElementById('payment-form');

form.addEventListener('submit', function (ev) {
    ev.preventDefault(); // Prevent the default form submission action
    card.update({ 'disabled': true }); // Disable the card input
    $('#submit-button').attr('disabled', true); // Disable the submit button
    stripe.confirmCardPayment(clientSecret, { // Begin the card confirmation process
        payment_method: {
            card: card, // Use the card we initialized earlier
        }
    }).then(function (result) {
        if (result.error) { // If an error occurred
            var errorDiv = document.getElementById('card-errors');
            var html = `
                <span class="icon" role="alert">
                <i class="fas fa-times"></i>
                </span>
                <span>${result.error.message}</span>`;
            $(errorDiv).html(html);
            card.update({ 'disabled': false }); // Re-enable the card input
            $('#submit-button').attr('disabled', false); // Re-enable the submit button
        } else {
            if (result.paymentIntent.status === 'succeeded') { // If the payment was successful
                form.submit(); // Submit the form
            }
        }
    });
});
