(function () {
    'use strict'
    let tooltipTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="tooltip"]'))
    tooltipTriggerList.forEach(function (tooltipTriggerEl) {
      new bootstrap.Tooltip(tooltipTriggerEl)
    })
  })()

const baseSocket = new WebSocket("ws://127.0.0.1:8001/chatstatus");

baseSocket.onopen = (evt) => {
    console.log("connection open");     
    baseSocket.send(JSON.stringify({"EVENT":"CHATSTATUS", "DATA":""})); 
}

baseSocket.onclose = (evt) => {console.log("connection closed: " + evt.reason + " : " + evt.code);}

baseSocket.onmessage = (message) => {
    console.log(message); 
    let eventData = JSON.parse(message.data)
    if(eventData.EVENT == "CHATSTATUS"){
        let chatStatus = eventData.DATA ? 'Connected' : "Disconnected"
        document.getElementById('chatstatus').innerHTML = "<i id='chatdot' class='bi bi-record-fill' style = 'color:red'></i>Chat Status: " + chatStatus;
        document.getElementById('chatdot').style = eventData.DATA ? 'color:yellow' : 'color:red';
        document.getElementById('chatAction').innerHTML = eventData.DATA ? "Disconnect" : "Connect";
        document.getElementById('chatAction').onclick = eventData.DATA ? disconnectChatServer : connectChatServer;
        let rooms = "Rooms: " 
        for(let room in eventData.ROOMS){
          if(room == 0)
            rooms += eventData.ROOMS[room]
          else
            rooms += ", " + eventData.ROOMS[room]

        }
        document.getElementById('rooms').innerHTML = eventData.DATA ?  rooms : ""
        document.getElementById('bot').innerHTML = eventData.DATA ?  "Bot Name: " + eventData.BOTNAME : ""
 
  }
}

baseSocket.onerror = (ws,evnt) =>{console.log(evnt); const socket = new WebSocket("ws://127.0.0.1:8001/chatstatus");}

function connectChatServer(){
  baseSocket.send(JSON.stringify({"EVENT":"CHATCONNECT", "DATA":""})); 
}

function disconnectChatServer(){
  baseSocket.send(JSON.stringify({"EVENT":"CHATDISCONNECT", "DATA":""})); 
}