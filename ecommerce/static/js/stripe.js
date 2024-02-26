// stripe.js
var stripe = Stripe('pk_test_51OcpcVCwVss9H8ocia5OoPwKsPMOwByDPgjvLvbWO9aq1tIaLfsY9vgAXCq8eQAZML2RSKX1WiLt1ENvjnCz4o570048rusYgz');
var elements = stripe.elements();

// Create an instance of the card Element.
var card = elements.create('card', {
    style: {
        base: {
            fontSize: '16px',
            color: '#32325d',
            fontFamily: '"Helvetica Neue", Helvetica, sans-serif',
            '::placeholder': {
                color: '#aab7c4',
            },
        },
        invalid: {
            color: '#fa755a',
        },
    },
});

// Add an instance of the card Element into the `card-element` div.
card.mount('#card-element');

// Handle real-time validation errors from the card Element.
card.addEventListener('change', function (event) {
    var displayError = document.getElementById('card-errors');
    if (event.error) {
        displayError.textContent = event.error.message;
    } else {
        displayError.textContent = '';
    }
});

// Handle form submission.
var form = document.getElementById('payment-form');
var submitButton = document.getElementById('submitbtn');

form.addEventListener('submit', function (event) {
    event.preventDefault();
    console.log(new FormData(form));

    stripe.createToken(card).then(function (result) {
        if (result.error) {
            // Inform the user if there was an error.
            var errorElement = document.getElementById('card-errors');
            errorElement.textContent = result.error.message;
        } else {
            // Send the token to your server.
            stripeTokenHandler(result.token);
        }
    });
});

function stripeTokenHandler(token) {
    var form = document.getElementById('payment-form');
    var hiddenInput = document.createElement('input');
    hiddenInput.setAttribute('type', 'hidden');
    hiddenInput.setAttribute('name', 'stripeToken');
    hiddenInput.setAttribute('value', token.id);
    form.appendChild(hiddenInput);

    // Submit the form to the handle_payment view.
    form.action = '/handle-payment/';
    form.submit();
}
