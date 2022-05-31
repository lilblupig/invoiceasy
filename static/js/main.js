// Declare variable to use ajax response
let hasSubs = "";

function checkSubs() {
    // Send ajax request to Django view to check for subs
    $.ajax({
        type: "GET",
        url: "/subscriptions/check-subs/",
        success: function(results) {
            hasSubs = results.subscribed;
        }
    });
};

// Stripe checkout code
// Get Stripe publishable key using Django view
fetch("/subscriptions/config/")
.then((result) => { return result.json(); })
.then((data) => {
    // Initialize Stripe.js
    const stripe = Stripe(data.publicKey);

    // Event handler when 'Subscribe' button clicked
    let submitBtn = document.querySelector("#submitBtn");
    if (submitBtn !== null) {
        submitBtn.addEventListener("click", () => {
            // Call checkSubs function, wait for response
            checkSubs();
            setTimeout(function(){
                if (hasSubs == true) {
                    $("#submitBtn").css("display", "none");
                    $("#subs-text").html("You seem to already be subscribed.");
                    $("#dash-btn").removeClass("hide-me");
                } else {
                    // Get Checkout Session ID
                    fetch("/subscriptions/create-checkout-session/")
                    .then((result) => { return result.json(); })
                    .then((data) => {
                        // Redirect to Stripe Checkout
                        return stripe.redirectToCheckout({sessionId: data.sessionId})
                    })
                }
            }, 300); // Duration of timeout for ajax request
        });
    }
});
