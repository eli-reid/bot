
const socket = new WebSocket("ws://127.0.0.1:8001");

socket.onopen = (evt) => {console.log("connection open")}

socket.onclose = (evt) => {console.log("connection closed: " + evt.reason + " : " + evt.code);}

socket.onmessage = (message) => {console.log(message)}

socket.onerror = (ws,evnt) =>{console.log(evnt);const socket = new WebSocket("ws://127.0.0.1:8001");}

function startt(){
    let eventDATA={};
    let timesplit = document.getElementById("time").value.split(':');
    eventDATA["Hr"] = timesplit[0];
    eventDATA["Min"] = timesplit[1];
    eventDATA["DisplayMsg"] = document.getElementById("display").value;
    eventDATA["EndMsg"] = "Time For Beds";
    let data = JSON.stringify(eventDATA);
    let event =  {"event":"EVENT_START","data": data };
    socket.send(JSON.stringify({"EVENT":1,"data": JSON.stringify(event)}));
}

function stopt(){
    let event =  {"event":"EVENT_STOP","data": ""};
    socket.send(JSON.stringify({"EVENT":1,"data": JSON.stringify(event)}));
}

function addHour(){
    let timesplit = document.getElementById("time").value.split(':');
    let hour = parseInt(timesplit[0]);
    let min = parseInt(timesplit[1]);
    let newHour = hour + 1;
    if (newHour > 23)
        hour = newHour - 24;
    else
        hour = newHour;

    if(min.toString().length<2)
        min = "0" + min;
    if(hour.toString().length<2)
        hour = "0" + hour;
    newTime = hour + ":" + min
    document.getElementById("time").value = newTime;
    startt();
}

function addmin(){
    let timesplit = document.getElementById("time").value.split(':');
    let hour = parseInt(timesplit[0]);
    let min = parseInt(timesplit[1]);
    let newMin = min + 15;
    if (newMin > 59){
        min = newMin - 60;
        let newHour = hour + 1;
        if (newHour > 23)
            hour = newHour - 24;
        else
            hour = newHour;
    }
    else
        min = newMin;

    if(min.toString().length<2)
        min = "0" + min;
    if(hour.toString().length<2)
        hour = "0" + hour;
    newTime = hour + ":" + min
    document.getElementById("time").value = newTime;
    startt()
} 
