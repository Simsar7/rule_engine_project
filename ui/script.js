document.getElementById('ruleForm').addEventListener('submit', function(event) {
    event.preventDefault(); // Prevent form submission
    
    const ruleInput = document.getElementById('rule').value;

    fetch('/create_rule', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ rule: ruleInput })
    })
    .then(response => response.json())
    .then(data => {
        if (data.error) {
            alert(data.error);
        } else {
            // Display the AST representation
            const astOutput = JSON.stringify(data.ast, null, 2); // Pretty-print JSON
            document.getElementById('astOutput').textContent = astOutput;
        }
    })
    .catch(error => console.error('Error:', error));
});

document.getElementById('evaluateForm').addEventListener('submit', function(event) {
    event.preventDefault(); // Prevent form submission
    

}