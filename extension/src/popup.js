// popup.js

document.getElementById('captureButton').addEventListener('click', function() {
  // Obter as keywords inseridas pelo usuário
  const keywords = document.getElementById('keywords').value;

  // Enviar mensagem para o content.js para capturar os dados
  chrome.tabs.query({ active: true, currentWindow: true }, function(tabs) {
    chrome.tabs.sendMessage(tabs[0].id, { action: "captureData" }, function(response) {
      console.log(response);  // Exibir os dados capturados no console
      // Construir a mensagem MCP
      const mcpMessage = {
        version: "1.0",
        operation: "create",
        context: {
          Prompt: response.title,
          Desc: response.content,
          URL: response.url,
          Keywords: keywords.split(',') // Converter a string de keywords em um array
        },
        metadata: {}
      };

      // Enviar a mensagem MCP para o servidor
      // ...
    });
  });
});