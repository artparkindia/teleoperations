"use strict"

var current_script = $('script[src*=rospub]'); 
var ws = current_script.attr('ws')
var websocket_url = "ws://"+ws+":9090" 
var ros = new ROSLIB.Ros({
    url : websocket_url
});

ros.on('connection', function() {
    console.log('Connected to websocket server', websocket_url);
});

ros.on('error', function(error) {
    alert('Error connecting to websocker server', error)
    console.log('Error connecting to websocket server: ', error);
});

ros.on('close', function() {
    console.log('Connection to websocket server closed.');
});

var coord_pub = new ROSLIB.Topic({
    ros : ros,
    name : '/coord',
    messageType : 'std_msgs/String'
});

var followme_pub = new ROSLIB.Topic({
    ros : ros,
    name : '/followme',
    messageType : 'std_msgs/Bool'
});

var status_listener = new ROSLIB.Topic({
    ros : ros,
    name: '/status',
    messageType: 'std_msgs/String'
});

var status_pub = new ROSLIB.Topic({
    ros : ros,
    name: '/status',
    messageType: 'std_msgs/String'
});