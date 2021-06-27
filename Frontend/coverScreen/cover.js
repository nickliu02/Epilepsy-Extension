// Get the modal
var modal = document.getElementById("myModal");

// Get the <span> element that closes the modal
var span = document.getElementsByClassName("close")[0];

var yes = document.getElementById("yes");

window.onload = function () {
  yes.addEventListener("click", () => {
    // Get active tab.
    chrome.tabs.query({ active: true }, (activeTabs) => {
      //modal.style.display = "none";
      window.close();
    });
  });
  span.addEventListener("click", () => {
    // Get active tab.
    chrome.tabs.query({ active: true }, (activeTabs) => {
      //modal.style.display = "none";
      window.close();
    });
  });
};
