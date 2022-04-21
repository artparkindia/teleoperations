#!/bin/bash

video="0"
ip="0.0.0.0"
app=$(readlink -f webapp.py)
follow_me="0"
while getopts v:i:f: x
do
	case "$x" in
	 v) video=${OPTARG};;
	 i) ip=${OPTARG};;
	 f) follow_me=${OPTARG};;
	esac
done
video_location="/dev/video$video"
echo "video:$video_location, ip:$ip"
if [ ! -e $video_location ]; then
	echo "video not found at $video_location"
	exit 1
fi

if [[ $follow_me -eq "0" ]]; then
	sudo docker run --device=$video_location -d --rm --name webrtc-streamer -p 8000:8000 -it mpromonet/webrtc-streamer 
fi
python3 $app -w $ip -f $follow_me &
source /opt/ros/noetic/setup.bash
roslaunch rosbridge_server rosbridge_websocket.launch
