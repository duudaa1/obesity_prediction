const form = document.getElementById('prediction-form');
const resultDiv = document.getElementById('result');

form.addEventListener('submit', function(e) {
    e.preventDefault();

    // Captura os dados preenchidos (exemplo com alguns campos)
    const gender = document.getElementById('gender').value;
    const age = document.getElementById('age').value;
    const weight = document.getElementById('weight').value;
    const height = document.getElementById('height').value;

    // Simula um cálculo simples (IMC só como exemplo)
    const bmi = weight / (height * height);

    let prediction = '';

    if (bmi < 18.5) {
        prediction = 'Abaixo do peso';
    } else if (bmi < 24.9) {
        prediction = 'Peso saudável';
    } else if (bmi < 29.9) {
        prediction = 'Sobrepeso';
    } else {
        prediction = 'Obesidade';
    }

    // Mostra o resultado na tela
    resultDiv.innerHTML = `<p>Resultado simulado com base no IMC: <strong>${prediction}</strong></p>`;

    // 🔥 Quando conectar ao backend Flask, você vai substituir esse código por uma requisição HTTP (fetch).
});
