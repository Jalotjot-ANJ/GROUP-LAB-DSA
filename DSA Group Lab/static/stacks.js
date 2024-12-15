document.addEventListener("DOMContentLoaded", function () {
    const form = document.getElementById("converter-form");
    const resultContainer = document.getElementById("result-container");
    const postfixResult = document.getElementById("postfix-result");

    form.addEventListener("submit", function (e) {
        e.preventDefault();

        // Get the input value
        const infixExpression = document.getElementById("infix-expression").value;

        // Send the data to the backend via fetch API
        fetch("/convert", {
            method: "POST",
            headers: {
                "Content-Type": "application/x-www-form-urlencoded",
            },
            body: `infix_expression=${encodeURIComponent(infixExpression)}`
        })
        .then(response => response.json())
        .then(data => {
            if (data.postfix) {
                postfixResult.innerText = data.postfix; // Show the postfix result
                resultContainer.style.display = "block"; // Make result visible
            } else {
                alert("Error converting expression. Please try again.");
            }
        })
        .catch(error => {
            console.error("Error:", error);
            alert("An error occurred while processing your request.");
        });
    });
});
