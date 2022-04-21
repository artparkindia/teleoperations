"use strict"

var current_script = $('script[src*=booktrip]'); 
var location_data = current_script.attr('location_data')
var last_activity_time = Date.now()
var CUTOFFTIME = 20*1000
var cancel_req = false

const status_code ={
    1:'ABORTED',
    2:'CANCELLED',
    3:'COMPLETED',
    4:'INTRANSIT'
}

location_data = JSON.parse(location_data)

function set_last_activity_time(){
    last_activity_time = Date.now()
}

status_listener.subscribe(function(message) {
    var id = JSON.parse(message.data)['id']
    // console.log('Received message on ' + status_listener.name + ': ' + id);
    document.getElementById('status_div').innerText = "Status: "+status_code[id]
    if(id==2 & cancel_req){
        button_start_emergency('START');
        cancel_req = false
    }
});

$("#go_button").click(function(){

    var location_val = $("#destination_select").val()
    var latlong = '0,0'
    if(location_val in location_data){
        latlong = location_data[location_val]
        publish_data(location_val, latlong, emergency)
    }else if(location_val != '-1'){
        alert(location_val+' coordinates not found')
    }    
    set_last_activity_time()
})

$("#destination_select").click(function(){
    set_last_activity_time()
})

function enable_ops(){
    document.getElementById('destination_select').disabled=false
    document.getElementById('go_button').disabled=false
}

function disable_ops(){
    document.getElementById('destination_select').disabled=true
    document.getElementById('go_button').disabled=true
}

$("#emergency_stop").click(function(){
    if(emergency){
        button_stop_emergency('CANCEL')
        enable_ops()
    }else{
        cancel_req = true
        publish_data()
        disable_ops()
        // button_start_emergency('START');
    }				
})

function publish_data(location='', latlong='', stop=true){
    var loc_msg =  new ROSLIB.Message({
        data:JSON.stringify({
            location,
            latlong,
            stop,   
            autonomy:true
        })
    })
    coord_pub.publish(loc_msg)
    return true
}

button_stop_emergency('CANCEL')

// setInterval(function(){ 
//     var current_time = Date.now()
//     if((current_time - last_activity_time)>CUTOFFTIME){
//         set_last_activity_time()
//         button_start_emergency()
//         // disable_ops()
//     }				
// }, 1000);

setInterval(function(){
    var loc_msg =  new ROSLIB.Message({
        data:JSON.stringify({
            id:Math.ceil(Math.random()*4)
        })
    })
    status_pub.publish(loc_msg)
}, 1000)