var btnConnect = document.getElementById('connect');
var btnDisConnect = document.getElementById('disconnect');
var btnStatus = document.getElementById('status');

console.log("Connecting..");

client = mqtt.connect('wss://test.mosquitto.org:8081/mqtt')
console.log('wss://test.mosquitto.org:8081/mqtt');

client.on("connect", function () {
  // client.subscribe("ricameonanitcherry")
  client.subscribe("ZAPIER")
  client.subscribe("BASH")
  client.subscribe("ELIXIR")
  console.log("Successfully connected");
  btnStatus.setAttribute('value', 'Sounds not yet detected!')
})

client.on("message", function (topic, payload) {
  // console.log([topic, payload].join(": "));
  console.log("Received { topic: " + topic + "; payload: " + payload + " }");
  btnStatus.setAttribute('value', payload)
  console.log(payload);


  if (payload != "Not Noisy") {
    btnStatus.setAttribute('class', 'btn btn-danger')
    let tbl = document.getElementById('receiver');
    let tbody = document.getElementById('msg');
    let tr = document.createElement('tr');
    let msgTopic = document.createElement('td');
    let msgPayload = document.createElement('td');
    let msgTime = document.createElement('td');
    msgTopic.appendChild(document.createTextNode(topic));
    msgPayload.appendChild(document.createTextNode(payload));
    msgTime.appendChild(document.createTextNode(moment().format('llll')));
    tr.appendChild(msgTopic);
    tr.appendChild(msgPayload);
    tr.appendChild(msgTime);
    tbody.appendChild(tr);
    tbl.appendChild(tbody);

  } else {
    btnStatus.setAttribute('class', 'btn btn-success')
  }
  if (payload != "Not Noisy") {
    alert(topic+" reached NOISY LEVEL!")
  }

})


