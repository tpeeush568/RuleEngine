document.addEventListener('DOMContentLoaded', function() {
    document.getElementById('submit-rule').addEventListener('click', function() {
        const rule = document.getElementById('rule').value;

        fetch('/rules', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ rule_string: rule })
        })
        .then(response => response.json())
        .then(data => {
            console.log('Rule submitted:',data);
        })
        .catch(error => console.error('Error:', error));
    });

    document.getElementById('submit-evaluation').addEventListener('click', function() {
        const rule = document.getElementById('rule').value;
        const data = document.getElementById('data').value;

        fetch('/evaluate', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ rule_string: rule, data: JSON.parse(data) })
        })
        .then(response => response.json())
        .then(data => {
            console.log('Evaluation result:', data); // Debugging line
            if (data.result !== undefined) {
                document.getElementById('result').textContent = `Evaluation Result: ${data.result}`;
            } else {
                document.getElementById('result').textContent = 'Evaluation failed';
            }
        })
        .catch(error => console.error('Error:', error));
    });
});
