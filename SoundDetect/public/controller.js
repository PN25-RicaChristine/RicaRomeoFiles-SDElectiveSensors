var btnConnect = document.getElementById('connect');
var btnDisConnect = document.getElementById('disconnect');
var btnStatus = document.getElementById('status');

console.log("Connecting..");

client = mqtt.connect('wss://test.mosquitto.org:8081/mqtt')
console.log('wss://test.mosquitto.org:8081/mqtt');

client.on("connect", function () {
  client.subscribe("ricameonanitcherry")
  console.log("Successfully connected");
  btnStatus.setAttribute('value', 'Sounds not yet detected!')
})

client.on("message", function (topic, payload) {
  // console.log([topic, payload].join(": "));
  console.log("Received { topic: " + topic + "; payload: " + payload + " }");
  btnStatus.setAttribute('value', payload)
  console.log(payload);
  btnStatus.setAttribute('class', 'btn btn-success')
})


