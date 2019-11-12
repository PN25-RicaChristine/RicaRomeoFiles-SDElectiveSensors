var btnConnect = document.getElementById('connect');
var btnDisConnect = document.getElementById('disconnect');
var btnStatus = document.getElementById('status');

console.log("Connecting..");

client = mqtt.connect('wss://test.mosquitto.org:8081/mqtt')
console.log('wss://test.mosquitto.org:8081/mqtt');

client.on("connect", function () {
  console.log("Successfully connected");
})
// basic functionalities
function connectFunc() {
  btnStatus.disabled = false;
  btnDisConnect.disabled = false;
  btnConnect.disabled = true;
  btnStatus.setAttribute('value', 'Laser is switched ON successfully!')
  console.log('Laser is switched ON successfully!');
  btnStatus.setAttribute('class', 'btn btn-success')

  client.publish('ricameo/temp', 'on');

  client.on("message", function (topic, payload) {
    // console.log([topic, payload].join(": "));
    console.log("Received { topic: " + topic + "; payload: " + payload + " }");

  })

}
// 

// basic functionalities
function disconnectFunc() {
  client.publish('ricameo/temp', 'off');
  btnStatus.disabled = true;
  btnDisConnect.disabled = true;
  btnConnect.disabled = false;
  console.log('Laser is switched OFF successfully!');
  console.log('Disconnected');
  btnStatus.setAttribute('value', 'Laser is switched OFF successfully!')
  btnStatus.setAttribute('class', 'btn btn-warning')

}


