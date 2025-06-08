document.addEventListener("DOMContentLoaded", function () {
  const form = document.getElementById("obesityForm");
  const heightInput = document.getElementById("height");
  const weightInput = document.getElementById("weight");

  // Altura: converter cm para metros automaticamente
  heightInput.addEventListener("blur", function () {
    let valor = this.value.replace(",", ".");
    const numero = parseFloat(valor);
    if (!isNaN(numero) && numero > 100) {
      this.value = (numero / 100).toFixed(2); // 160 → 1.60
    }
  });

  // Peso: substituir vírgula por ponto sem alterar casas decimais
  weightInput.addEventListener("blur", function () {
    this.value = this.value.replace(",", ".");
  });

  // Envio do formulário
  form.addEventListener("submit", async function (event) {
    event.preventDefault();

    const formData = new FormData(form);
    const data = {};

    formData.forEach((value, key) => {
      // Converte strings numéricas para números reais
      if (!isNaN(value) && value.trim() !== "") {
        data[key] = parseFloat(value);
      } else {
        data[key] = value;
      }
    });

    try {
      const response = await fetch("https://full-health.onrender.com/prever", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify(data),
      });

      if (!response.ok) {
        throw new Error("Erro ao comunicar com a API");
      }

      const resultado = await response.json();

      // Exibir resultado
      const popup = document.getElementById("resultado");
      const texto = document.getElementById("resultado-texto");
      texto.innerText = "Classificação prevista: " + resultado.classificacao_obesidade;
      popup.style.display = "block";
    } catch (erro) {
      console.error("Erro:", erro);
      alert("Erro ao processar a requisição.");
    }
  });
});
