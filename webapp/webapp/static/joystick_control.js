"use strict"

document.getElementById("video").controls  = false
// Create Joystick objects
var Joy1 = new JoyStick('joy1Div');
var CUTOFFTIME = 20*1000
Joy1.Disable()
var last_activity_time = Date.now()

function publish_data(x=0, y=0, direction='C', stop=true){
    var coord_msg =  new ROSLIB.Message({
        data:JSON.stringify({
            stop,
            x,
            y,
            direction,
            autonomy:false
        })
    })
    // console.log(coord_msg)
    coord_pub.publish(coord_msg)
    return true
}

function set_last_activity_time(){
    last_activity_time = Date.now()
}

$("#joystick").on('mousedown touchstart touchend touchmove mouseup mousemove', function(){
    set_last_activity_time()
})

function disable_joystick(){
    publish_data()
    Joy1.Disable()
    button_start_emergency()
}

function enable_joystick(){
    Joy1.Enable()
    button_stop_emergency()
}

$("#emergency_stop").click(function(){
    if(emergency){
        button_stop_emergency()
        enable_joystick()
        set_last_activity_time()
    }else{
        button_start_emergency()
        disable_joystick();
    }				
})

setInterval(function(){ 
    var joy1Xvar = Joy1.GetX();
    var joy1Yvar = Joy1.GetY();
    var direction = Joy1.GetDir()
    var x = emergency ? 0:joy1Xvar;
    var y  = emergency ? 0:joy1Yvar;
    publish_data(x=x, y=y, direction=direction, stop=emergency)
    if(x!=0 || y!=0){
        set_last_activity_time()
    }
}, 100);

setInterval(function(){ 
    var current_time = Date.now()
    if(Joy1.GetX()==0 && Joy1.GetY()==0 && (current_time - last_activity_time)>CUTOFFTIME){
        disable_joystick()
        set_last_activity_time()
    }				
}, 1000);