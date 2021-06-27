//alert("working!");

let intervals = [];
let goto = 0;

setInterval(function () {
  console.log(intervals);
  var video = document.getElementsByTagName("video")[0];
  if (video) {
    let time = video.currentTime;
    for (let i = 0; i < intervals.length; i++) {
      if (time >= intervals[i][0] && time <= intervals[i][1]) {
        goto = intervals[i][1];

        continueScript();
        video.currentTime = goto
        video.pause();
        console.log("here");
      }
    }
  }
}, 1000);

chrome.runtime.onMessage.addListener(function (request, sender, sendResponse) {
  alert(window.location.toString());

  let data = { url: window.location.toString() };
  if (request.message) {
    data = { url: request.message };
    chrome.tabs.create({ url: request.message });
  }

  fetch("http://127.0.0.1:5000/check", {
    method: "POST",
    mode: "cors",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify(data),
  }).then((res) => {
    res.json().then((json) => {
      console.log(json);
      intervals = json.intervals;
    });
  });
});

function newPopup(url) {
  popupWindow = window.open(
    url,
    "popUpWindow",
    "height=800,width=1000,left=10,top=10,resizable=yes,scrollbars=yes,toolbar=yes,menubar=no,location=no,directories=no,status=yes"
  );
}

