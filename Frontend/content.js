function newPopup(url) {
  popupWindow = window.open(
    url,
    "popUpWindow",
    "height=800,width=1000,left=10,top=10,resizable=yes,scrollbars=yes,toolbar=yes,menubar=no,location=no,directories=no,status=yes"
  );
}

function continueScript() {
  newPopup(chrome.extension.getURL("./coverScreen/cover.html"));
}

function onClickButton() {
  window.open(chrome.runtime.getURL("/coverScreen/cover.html"));
}

let intervals = [];
let goto = 0;

setInterval(function (request) {
  console.log(intervals);
  var video = document.getElementsByTagName("video")[0];
  if (video) {
    let time = video.currentTime;
    for (let i = 0; i < intervals.length; i++) {
      if (time >= intervals[i][0] && time < intervals[i][1]) {
        goto = intervals[i][1];
        intervals.shift();

        //continueScript();
        video.currentTime = goto;
        console.log("here");
        break;
      }
    }
  }
}, 1000);

/* 
chrome.browserAction.onClicked.addListener(function (tab) {
  chrome.windows.create(
    {
      url: chrome.runtime.getURL("./coverScreen/cover.html"),
      type: "popup",
      incognito: split,
    },
    function (tab) {
      // Tab opened.
    }
  );
}); 
*/

chrome.runtime.onMessage.addListener((request, sender, sendResponse) => {
  console.log("here2");
  if (request.message === "popup") {
    chrome.tabs.create({
      url: chrome.runtime.getURL("./coverScreen/cover.html"),
    });
  }
});

chrome.runtime.onMessage.addListener(function (request, sender, sendResponse) {
  //alert(window.location.toString());

  let data = { url: window.location.toString() };
  if (request.message) {
    data = { url: request.message };
    chrome.tabs.create({ url: request.message });
  }

  if (request.message === "popup") {
    console.log("here2");
    chrome.tabs.create({
      url: chrome.runtime.getURL("./coverScreen/cover.html"),
    });
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

//FOLLOWING CODE USED FOR PLAY AND PAUSE

/* chrome.runtime.onMessage.addListener(function (request, sender, sendResponse) {
  if (request.message === "toggle_video_state") {
    var video = document.getElementsByTagName("video")[0];
    if (video) {
      if (video.paused) {
        video.play();
        sendResponse({ paused: false, tabId: request.tabId });
      } else {
        video.pause();
        sendResponse({ paused: true, tabId: request.tabId });
      }
    } else {
      sendResponse({ error: "No video object found" });
    }
  }
}); */
