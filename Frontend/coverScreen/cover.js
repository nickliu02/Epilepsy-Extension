// Get the modal
var modal = document.getElementById("myModal");

// Get the <span> element that closes the modal
var span = document.getElementsByClassName("close")[0];

var yes = document.getElementById("yes");
// When the user clicks the button, open the modal

// When the user clicks on <span> (x), close the modal
/* span.onclick = function () {
  window.close();
};

yes.onclick = function () {
  window.close();
};

// When the user clicks anywhere outside of the modal, close it
window.onclick = function (event) {
  if (event.target == modal) {
    window.close();
  } 
}
*/
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
