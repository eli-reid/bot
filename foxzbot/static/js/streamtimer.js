// JavaScript source code
let a = 0
let eventData
let timeinterval 
let timedata = {}
var event = {}
const socket = new WebSocket("ws://127.0.0.1:8001/streamtimer");


function TimeDiff() {
    let Start = new Date();
    let End = new Date(Start.getFullYear(), Start.getMonth(), Start.getDate(), eventData.Hr, eventData.Min, 00)
    if (End<Start) {
        End = new Date(Start.getFullYear(), Start.getMonth(), Start.getDate() + 1,eventData.Hr, eventData.Min, 00)
    }
    let d = End - Start;
    let hours = Math.floor((d % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
    let minutes = Math.floor((d % (1000 * 60 * 60)) / (1000 * 60));
    let seconds = Math.floor((d % (1000 * 60)) / 1000);
    if (minutes < 10) { minutes = "0" + minutes; } 
    if (seconds < 10) { seconds = "0" + seconds;} 
    
    if (hours == 0 && minutes == 0 && seconds == 0) {
        clearInterval(timeinterval);
        timeinterval=0;
        $("#displayMsg").html(eventData.EndMsg);
        $("#hours").html("");
        $("#minutes").html("");
        $("#seconds").html("");
    }
    else {
        $("#hours").html(hours + ":");
        $("#minutes").html(minutes + ":");
        $("#seconds").html(seconds);
    }
}

socket.onmessage = (message) => {
    let socketMessage = JSON.parse(message.data);
    console.log(message.data)
    switch (socketMessage.event) {
        case "EVENT_STOP":
            clearInterval(timeinterval);
            timeinterval=0 ;
            $("#displayMsg").html("Timer Stopped!");
            $("#hours").html("");
            $("#minutes").html("");
            $("#seconds").html("");
            $("#debug").html("socket data: " + socketMessage.data) ;
            break;

        case "EVENT_START":    
        case "EVENT_UPDATE":
        case "EVENT_ADD_MIN":
        case "EVENT_ADD_HOUR":
            eventData = JSON.parse(socketMessage.data);
            $("#displayMsg").html(eventData.DisplayMsg);
            if (!timeinterval) 
                timeinterval = setInterval(TimeDiff, 1000);
            break;
    }
   
} 


