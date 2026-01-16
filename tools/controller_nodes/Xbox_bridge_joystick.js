const Joystick = require('joystick');
const WebSocket = require('ws');

// Connect to ESP32 rover
const ws = new WebSocket('ws://192.168.0.168:81');

// Joystick setup (device 0 = /dev/input/js0)
const joystick = new Joystick(0, 3500, 350);

ws.on('open', () => console.log("✅ WebSocket Connected!"));
ws.on('error', (err) => console.log("❌ WebSocket Error:", err.message));

// Axis events
joystick.on('axis', (event) => {
  const { number, value } = event;
  let command = null;

  // Left stick vertical (axis 1): Forward/Backward
  if (number === 1) {
    if (value < -0.5) command = "FWD";
    else if (value > 0.5) command = "BACK";
    else command = "STOP";
  }

  // Right stick horizontal (axis 3): Left/Right
  if (number === 3) {
    if (value < -0.5) command = "LEFT";
    else if (value > 0.5) command = "RIGHT";
  }

  if (command && ws.readyState === WebSocket.OPEN) {
    ws.send(command);
    console.log("➡️ Sent:", command);
  }
});

// Button events
joystick.on('button', (event) => {
  if (event.value === 1) {
    let cmd = null;
    switch (event.number) {
      case 0: cmd = "A"; break;
      case 1: cmd = "B"; break;
      case 2: cmd = "X"; break;
      case 3: cmd = "Y"; break;
      case 5: cmd = "RB"; break;
      case 4: cmd = "LB"; break;
    }

    if (cmd && ws.readyState === WebSocket.OPEN) {
      ws.send(cmd);
      console.log("🎮 Button:", cmd);
    }
  }
});
