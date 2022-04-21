# copernicus

To run the webapp for teledriving

* Pre-requisties
  * pip3 install -r requirements.txt 
  * [Ros Melodic](http://wiki.ros.org/melodic/Installation/Ubuntu) <b>Note</b>: If using a different version change in start.sh 
  * [Ros Bridge](http://wiki.ros.org/rosbridge_suite/Tutorials/RunningRosbridge) 
  * docker pull mpromonet/webrtc-streamer

* Start the webapp ( Two modes : Teleops-Autonomy and Follow me)
   * Teleops/Autonomy mode
      * cd webapp
      * ```./start.sh -i <machine-ip-address> -v <video number as in /dev/video>``` 
      * In the browser open the page \<ip-address>:5000 
      * Coordinates are published on a ```ros1 topic /coord``` only on button(GO) press
   * Follow-Me 
      * cd webapp
      * ```./start.sh -i <machine-ip-address> -f 1 ```
      * In the browser open the page \<ip-address>:5000
      * Start/Stop value in Boolean is published on a ```ros1 topic /followme``` only on button(START/STOP) press

* Cleanup 
  * ```./cleanup.sh```
