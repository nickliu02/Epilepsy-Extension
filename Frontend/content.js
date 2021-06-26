//alert("working!");
chrome.runtime.onMessage.addListener(function (request) {
  alert(request);
});
