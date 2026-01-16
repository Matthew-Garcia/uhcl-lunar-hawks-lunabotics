const WebSocket = require('ws');
const HID = require('node-hid');

// Update with your vendorId and productId
const vendorId = 0x045E;   // Sony (1356 in decimal)
const productId = 0x0B13;  // DualSense Controller

// Initialize WebSocket Client
const ws = new WebSocket('ws://192.168.0.54:81');  // <-- Change to your ESP32 IP address

let isConnected = false;

// WebSocket connection events
ws.on('open', () => {
  console.log("WebSocket Connected!");
  isConnected = true;
});

ws.on('error', (error) => {
  console.log("WebSocket Error: ", error.message);
});

ws.on('close', () => {
  console.log("WebSocket Disconnected.");
  isConnected = false;
});

// Initialize Controller
const device = new HID.HID(vendorId, productId);

console.log("🎮 Controller Connected!");

// Event Listener for Joystick Data
device.on("data", (data) => {
  const leftStickX = data[2];
  const leftStickY = data[2];
  //const rightStickX = data[2];
  //const rightStickY = data[5];

  if (isConnected) {
    const joystickData = {
      lx: leftStickX,
      ly: leftStickY,
    //  rx: rightStickX,
     // ry: rightStickY
    };

    ws.send(JSON.stringify(joystickData));
    console.clear();
    console.log("📡 Sending Joystick Data:");
    console.log(joystickData);
  } else {
    console.log("WebSocket not connected yet.");
  }
});

