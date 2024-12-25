// content.js

import TurndownService from './turndown.js'; // Importar a biblioteca turndown

// Função para capturar o título da página
function getPageTitle() {
  return document.title;
}

// Função para capturar o conteúdo da página em Markdown
function getPageContent() {
  // Usar a biblioteca turndown para converter HTML para Markdown
  const turndownService = new TurndownService();
  return turndownService.turndown(document.body.innerHTML);
}

// Função para capturar a URL da página
function getPageUrl() {
  return window.location.href;
}

// Listener para receber mensagens do popup.js
chrome.runtime.onMessage.addListener(function(request, sender, sendResponse) {
   // Verificar se a mensagem é para capturar os dados
  if (request.action === "captureData") {
    // Capturar o título da página
    const title = getPageTitle();
    // Capturar o conteúdo da página
    const content = getPageContent();
    // Capturar a URL da página
    const url = getPageUrl();

    // Enviar os dados para o popup.js
    sendResponse({
      title: title,
      content: content,
      url: url
    });
  }
});