var socket;

function getDateTime() {
	var d = new Date();
	var curr_date = d.getDate();
	var curr_month = d.getMonth();
	curr_month++;
	var curr_year = d.getFullYear();
	var curr_hour = d.getHours();
	var curr_min = d.getMinutes();
	var curr_sec = d.getSeconds();
	var curr_msec = d.getMilliseconds();
	var vDateTime = (curr_month + "/" + curr_date + "/" + curr_year + " " + curr_hour + ":" + curr_min + ":" + curr_sec + ":" + curr_msec);
	return vDateTime;
}

function log(msg) {
	var log_window = document.getElementById("log");
	var timestamp = getDateTime();
	log_window.innerHTML += '<br />' + timestamp + ":  " + msg;
	log_window.scrollTop = log_window.scrollHeight;
}

function init() {
	//websocket server to connect to
	var host = "ws://192.168.1.133:8765/";

	//let's try to connect
	try {
		socket = new WebSocket(host);
		log('WebSocket - status ' + socket.readyState);

		socket.onopen = function(msg) {
			if (this.readyState == 1) {
				log("We are now connected to websocket server. readyState = " + this.readyState);
			}
		};

		//Message received from websocket server
		socket.onmessage = function(msg) {
			log(" [ + ] Received: " + msg.data);
		};

		//Connection closed
		socket.onclose = function(msg) {
			log("Disconnected - status " + this.readyState);
		};

		socket.onerror = function() {
			log("Error");
		};
	} catch(ex) {
		log('Exception occured : ' + ex);
	}

	document.getElementById("msg").focus();
}

function send(msg) {
	if (!msg) {
		msg = "EMPTY COMMAND";
	}

	try {
		socket.send(msg);
		log('Sent : ' + msg);
	} catch(ex) {
		log(ex);
	}
}

function quit() {
	if (socket != null) {
		log("Goodbye!");
		socket.close();
		socket = null;
	}
}

function reconnect() {
	quit();
	init();
}





//array of gpio pins and states
function switchGPIO(gpio) {

	//get current state
	var currentState = document["gpio" + gpio].src.indexOf("off.png");

	//if currentstate is not -1 the switch is off
	if (currentState != -1) {
		//its off turn the gpio on and switch the graphic
		send(gpio + " on");
		document["gpio" + gpio].src = "img/on.png";
	} else {
		//its on turn the gpio off and switch the graphic
		send(gpio + " off");
		document["gpio" + gpio].src = "img/off.png";
	}

}

