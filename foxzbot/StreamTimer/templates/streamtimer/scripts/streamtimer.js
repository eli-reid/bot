// JavaScript source code
let a = 0
let eventData
let timeinterval 
let timedata = {}

$(document).ready(function () {
    connectWebsocket(); 
});

function TimeDiff() {
    let Start = new Date()
    let End = new Date(Start.getFullYear(), Start.getMonth(), Start.getDate(), eventData.Hr, eventData.Min, 00)
    if (End<Start) {
        End = new Date(Start.getFullYear(), Start.getMonth(), Start.getDate() + 1,eventData.Hr, eventData.Min, 00)
    }
    let d = End - Start
    let hours = Math.floor((d % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
    let minutes = Math.floor((d % (1000 * 60 * 60)) / (1000 * 60));
    let seconds = Math.floor((d % (1000 * 60)) / 1000);
    if (minutes < 10) { minutes = "0" + minutes } 
    if (seconds < 10) { seconds = "0" + seconds } 
    
    if (hours == 0 && minutes == 0 && seconds == 0) {
        clearInterval(timeinterval)
        timeinterval=0
        $("#displayMsg").html(eventData.EndMsg)
        $("#hours").html("")
        $("#minutes").html("")
        $("#seconds").html("")
    }
    else {
        $("#hours").html(hours + ":")
        $("#minutes").html(minutes + ":")
        $("#seconds").html(seconds)
    }
}
function connectWebsocket() {
    let socket = new WebSocket("ws://127.0.0.1:3337/streamlabs");
    socket.onopen = function () {

        let auth = {
            author: "Edog0049a",
            website: "edog0049a.com",
            api_key: API_Key,
            events: [
                "EVENT_START", 
                "EVENT_STOP",
                "EVENT_UPDATE",
                "EVENT_ADD_MIN",
                "EVENT_ADD_HOUR",
                "EVENT_END"
            ]
        };
 
        socket.send(JSON.stringify(auth));
    };

    socket.onmessage = function (message) {
        let socketMessage = JSON.parse(message.data);
        $("#check").html(socketMessage.event)
        switch (socketMessage.event) {
            case "EVENT_START":
                eventData = JSON.parse(socketMessage.data);
                $("#displayMsg").html(eventData.DisplayMsg)
                if (!timeinterval) {
                    timeinterval = setInterval(TimeDiff, 1000);
                    $("#debug").html("socket data: " + socketMessage.data) 
                }
                else
                    $("#debug").html("already running: ") 
                break;
            case "EVENT_STOP":
                clearInterval(timeinterval)
                timeinterval=0 
                $("#debug").html("socket data: " + socketMessage.data) 
                break;
            case "EVENT_UPDATE":
                $("#debug").html("socket data: " + socketMessage.data) 
                eventData = JSON.parse(socketMessage.data);
                if (!timeinterval) 
                    timeinterval = setInterval(TimeDiff, 1000);
                break;
            case "EVENT_ADD_MIN":
                eventData = JSON.parse(socketMessage.data);
                $("#debug").html("socket data: " + socketMessage.data) 
                if (!timeinterval) 
                    timeinterval = setInterval(TimeDiff, 1000);
                break;
            case "EVENT_ADD_HOUR":
                $("#debug").html("socket data: " + socketMessage.data) 
                eventData = JSON.parse(socketMessage.data);
                if (!timeinterval) 
                    timeinterval = setInterval(TimeDiff, 1000);
                break;
            case "EVENT_END":

                break;
            default:
        }
        
    }
}