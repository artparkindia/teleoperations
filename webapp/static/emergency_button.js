"use strict"

var emergency=true

function update_button(removeClass, addClass, text){
    $("#emergency_stop").removeClass(removeClass)
    $("#emergency_stop").addClass(addClass)
    $("#emergency_stop").text(text)
}

function button_start_emergency(button_name='START'){
    emergency = true
    var addClass = 'btn-success'
    var removeClass = 'btn-danger'
    var text=button_name
    update_button(removeClass=removeClass, addClass=addClass, text=text)
}

function button_stop_emergency(button_name='STOP'){
    emergency = false
    var addClass = 'btn-danger'
    var removeClass = 'btn-success'
    var text = button_name
    update_button(removeClass=removeClass, addClass=addClass, text=text)
}