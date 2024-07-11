// Function to click all elements with the class 'colab-run-button'
function clickAllRunButtons() {
    // Select all elements with the class 'colab-run-button'
    const elements = document.querySelectorAll('colab-run-button');

    // Iterate over each element and click it
    elements.forEach(element => {
        element.click();
    });
}


function checkAndClickButton() {
    const connect_button = document.querySelector('#top-toolbar > colab-connect-button').shadowRoot.querySelector('#connect');
    const tooltipText = connect_button.getAttribute('tooltipText').trim().replace(/\s+/g, ' ');
    if (tooltipText === 'Click to connect' || tooltipText === 'Connect to a new runtime') {
        connect_button.click();
        clickAllRunButtons();
    }
}

setInterval(checkAndClickButton, 1000);
