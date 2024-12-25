const turndownService = new TurndownService();

function getPageTitle() {
  return document.title;
}

function getPageContent() {
  return turndownService.turndown(document.body.innerHTML);
}

function getPageUrl() {
  return window.location.href;
}

chrome.runtime.onMessage.addListener(function(request, sender, sendResponse) {
  if (request.action === "captureData") {
    const title = getPageTitle();
    const content = getPageContent();
    const url = getPageUrl();

    sendResponse({
      title: title,
      content: content,
      url: url
    });
  }
  return true;
});