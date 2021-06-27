var matchUrl = "*://www.youtube.com/watch?v*";
var queryInfo = { url: matchUrl };
document.addEventListener(
  "DOMContentLoaded",
  function () {
    document
      .getElementById("vidButton")
      .addEventListener("click", onClickVidButton, false);
    document
      .getElementById("myBtn")
      .addEventListener("click", continueScript, false);

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
    /*   function onClickButton() {
      var url = chrome.extension.getURL("./coverScreen/cover.html");
      window.open(url);
    } */
  },
  false
);

function newPopup(url) {
  popupWindow = window.open(
    url,
    "popUpWindow",
    "height=800,width=1000,left=10,top=10,resizable=yes,scrollbars=yes,toolbar=yes,menubar=no,location=no,directories=no,status=yes"
  );
}

window.onload = function () {
  var link = document.getElementById("myBtn");
  link.addEventListener("click", continueScript);
};
function continueScript() {
<<<<<<< Updated upstream
  newPopup("./coverScreen/cover.html");
  /*   chrome.tabs.query({ active: true, currentWindow: true }, function (tabs) {
    var tab = tabs[0];
    chrome.tabs.update(tab.id, {
      url: chrome.extension.getURL("./coverScreen/cover.html"),
    });
  }); */
=======
  chrome.tabs.query({ currentWindow: true, active: true }, function (tabs) {
    chrome.tabs.sendMessage(
      tabs[0].id,
      newPopup("./coverScreen/cover.html")
    );
  });
>>>>>>> Stashed changes
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
