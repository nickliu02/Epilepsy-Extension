var matchUrl = "*://www.youtube.com/watch?v*";
var queryInfo = { url: matchUrl };
document.addEventListener(
  "DOMContentLoaded",
  function () {
    document
      .getElementById("vidButton")
      .addEventListener("click", onclick, false);

    function onclick() {
      chrome.tabs.query({ currentWindow: true, active: true }, function (tabs) {
        chrome.tabs.sendMessage(tabs[0].id, "hi");
        //document.getElementsByName("video")[0].onpause();
      });
    }
  },
  false
);

//CODE USED FOR PLAY AND PAUSE
/* chrome.tabs.addListener(function (tabId, changeInfo, tab) {
  var re = /www\.youtube\.com/;
  if (re.test(tab.url) && changeInfo.title) {
    document.getElementById("title" + tabId).textContent = changeInfo.title;
    document.getElementById("url" + tabId).textContent = tab.url;
  }
});
 */
