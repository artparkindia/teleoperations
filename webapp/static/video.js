"use strict"

var webRtcServer  = null;
var device = null;
window.onload  = function() {
    var url = location.protocol+"//"+window.location.hostname+":8000"
    webRtcServer      = new WebRtcStreamer("video",url);
    fetch(url + "/api/getMediaList")
        .then( (response) => response.json() ) 
        .then( (response) => {
            device=response[0].video;
            webRtcServer.connect(device)
        })
        .catch((error) => {
            alert('error in geting the video device!')
            console.log('error:', error)
        })
}
window.onbeforeunload = function() { webRtcServer.disconnect(); }