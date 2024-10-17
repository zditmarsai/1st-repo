document.getElementById('healthForm').addEventListener('submit', function(event) {
    event.preventDefault();  // Prevent form submission from reloading the page

    // Get the condition input from the user
    const condition = document.getElementById('condition').value;

    // Ensure condition is not empty
    if (!condition) {
        document.getElementById('response').textContent = "Please enter a condition.";
        return;
    }

    // Show the loading spinner
    document.getElementById('spinner').style.display = 'block';

    // Construct the URL dynamically based on the user input
    const apiUrl = `http://127.0.0.1:8000/health-info/?condition=${encodeURIComponent(condition)}`;

    // Clear any previous responses or errors
    document.getElementById('response').textContent = JSON.stringify(data, null, 2);
;

    // Fetch the health information for the entered condition
    fetch(apiUrl)
        .then(response => {
            if (!response.ok) {
                throw new Error(`HTTP error! Status: ${response.status}`);
            }
            return response.json();  // Parse the JSON response
        })
        .then(data => {
            // Hide the loading spinner
            document.getElementById('spinner').style.display = 'none';

            // Display the JSON response in a readable format
            document.getElementById('response').textContent = JSON.stringify(data, null, 2);
        })
        .catch(error => {
            // Hide the loading spinner
            document.getElementById('spinner').style.display = 'none';

            // Display any errors
            document.getElementById('response').textContent = `Error fetching health information: ${error.message}`;
        });
});
