var matchUrl = "*://www.youtube.com/watch?v*";
var queryInfo = { url: matchUrl };
document.addEventListener(
  "DOMContentLoaded",
  function () {
    document
      .getElementById("vidButton")
      .addEventListener("click", onClickVidButton, false);
    /*   document
      .getElementById("linkButton", onClickLinkButton, false)
      .addEventListener("click"); */
    document
      .getElementById("myBtn")
      .addEventListener("click", onClickButton, false);

    function onClickVidButton() {
      chrome.tabs.query({ currentWindow: true, active: true }, function (tabs) {
        chrome.tabs.sendMessage(tabs[0].id, "");

        //document.getElementsByName("video")[0].onpause();
      });
    }
    function onClickLinkButton() {
      chrome.tabs.query({ currentWindow: true, active: true }, function (tabs) {
        chrome.tabs.sendMessage(
          tabs[0].id,
          document.getElementById("link").value
        );
      });
    }
    function onClickButton() {
      var url = chrome.extension.getURL("./coverScreen/cover.html");
      window.open(url);
    }
  },
  false
);

function continueScript() {
  newPopup("./coverScreen/cover.html");
}

//CODE USED FOR PLAY AND PAUSE
/* chrome.tabs.addListener(function (tabId, changeInfo, tab) {
  var re = /www\.youtube\.com/;
  if (re.test(tab.url) && changeInfo.title) {
    document.getElementById("title" + tabId).textContent = changeInfo.title;
    document.getElementById("url" + tabId).textContent = tab.url;
  }
});
 */
