document.getElementById('prediction-form').addEventListener('submit', function(event) {
    event.preventDefault();

     // Show loading indicator
     document.getElementById('prediction-result').innerHTML = '<p>Loading...</p>';

    // Get form data
    const formData = new FormData(event.target);

    // Send POST request to Flask API
    fetch('/predict', {
        method: 'POST',
        body: formData,
    })
    .then(response => response.json())
    .then(data => {
        // Display prediction result
        document.getElementById('prediction-result').innerHTML = `<p>Resources required: ${data.prediction} %</p>`;
    })
    .catch(error => console.error('Error:', error));
  });

  // Function to update slider value based on text field input
  function updateSlider(input, index) {
    var slider = document.getElementById('sliderValue' + index);
    var value = parseFloat(input.value);
    if (isNaN(value)) {
      input.value = slider.value;
    } else {
      slider.value = value;
    }
    updateSliderValue(slider, index);
  }

  // Function to update text field value based on slider input
  function updateSliderValue(slider, index) {
    var value = parseFloat(slider.value);
    var textField = document.getElementById('textFieldValue' + index);
    textField.value = value;
    // Update the output of the slider
    var output = document.getElementById('output' + index);
    output.textContent = value.toLocaleString();
    // Update the corresponding --text-value CSS variable
    slider.parentNode.style.setProperty('--text-value' + index, value);
  }

  // Function to update text field value based on slider input
  function updateTextFieldValue(slider, index) {
    var value = parseFloat(slider.value);
    var textField = document.getElementById('textFieldValue' + index);
    textField.value = value;
    // Update the output of the slider
    var output = document.getElementById('output' + index);
    output.textContent = value.toLocaleString();
    // Update the corresponding --text-value CSS variable
    slider.parentNode.style.setProperty('--text-value' + index, value);
  }
  