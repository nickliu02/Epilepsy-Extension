//alert("working!");

let intervals = {}

chrome.runtime.onMessage.addListener(function (request) {
    alert(window.location.toString());

    let data = {"url": window.location.toString()};
    if (request.message){
        data = {"url":request.message}
        chrome.tabs.create({url:request.message})

    }

    fetch("http://127.0.0.1:5000/check",{
        method:"POST",
        mode:"cors",
        headers:{
            'Content-Type':'application/json'
        },
        body:JSON.stringify(data)
    }).then(res => {
        res.json().then(json => {
            console.log(json.body);
            intervals = json.body.intervals
        });
    })

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
