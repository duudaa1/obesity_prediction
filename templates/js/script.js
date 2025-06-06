document.addEventListener("DOMContentLoaded", function () {
  const form = document.getElementById("obesityForm");

  form.addEventListener("submit", async function (event) {
    event.preventDefault();

    const formData = new FormData(form);
    const data = {};

    // Converte FormData para objeto com os valores corretos
    formData.forEach((value, key) => {
      // Converte para número quando apropriado
      if (!isNaN(value) && value.trim() !== "") {
        data[key] = parseFloat(value);
      } else {
        data[key] = value;
      }
    });

    try {
      const response = await fetch("http://127.0.0.1:8000/prever", {
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

      // Exibir o resultado da predição
      const output = document.getElementById("resultado");
      output.innerText = "Classificação prevista: " + resultado.classificacao_obesidade;

    } catch (erro) {
      console.error("Erro:", erro);
      alert("Falha na comunicação com o servidor.");
    }
  });
});
