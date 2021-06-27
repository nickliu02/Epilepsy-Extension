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
      .addEventListener("click", continueScript, false);

    function onClickVidButton() {
      chrome.tabs.query({ currentWindow: true, active: true }, function (tabs) {
        chrome.tabs.sendMessage(tabs[0].id, "");
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
  newPopup("./coverScreen/cover.html");
}
