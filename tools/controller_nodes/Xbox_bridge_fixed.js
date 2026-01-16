const WebSocket = require('ws');
const Joystick = require('joystick');

// Connect to your ESP32 Rover
const ws = new WebSocket('ws://192.168.0.168:81');
const joystick = new Joystick(0, 3500, 350);

let isConnected = false;

// WebSocket setup
ws.on('open', () => {
  console.log("✅ WebSocket Connected to Rover!");
  isConnected = true;
});

ws.on('error', (err) => console.log("⚠️ WebSocket Error:", err.message));
ws.on('close', () => {
  console.log("❌ WebSocket Disconnected.");
  isConnected = false;
});

console.log("🎮 Listening for joystick input...");

// Debounce for boost controls
let lastBoost = 0;
let lastBoostDecrease = 0;
let boostPressed = false;
let boostDecreasePressed = false;
const cooldownTime = 500;

// Axis events (movement)
joystick.on('axis', (event) => {
  if (!isConnected) return;

  // Left stick Y → forward/backward
  if (event.number === 1) {
    if (event.value < -10000) { ws.send("FWD"); console.log("Forward"); }
    else if (event.value > 10000) { ws.send("BACK"); console.log("Backward"); }
    else { ws.send("STOP"); }
  }

  // Right stick X → steering
  if (event.number === 3) {
    if (event.value < -10000) { ws.send("LEFT"); console.log("Left Turn"); }
    else if (event.value > 10000) { ws.send("RIGHT"); console.log("Right Turn"); }
    else { ws.send("STRAIGHT"); }
  }
});

// Button events
joystick.on('button', (event) => {
  if (!isConnected) return;

  switch (event.number) {
    case 0: if (event.value === 1) { ws.send("X"); console.log("Excavator"); } break;
    case 3: if (event.value === 1) { ws.send("Y"); console.log("Dump"); } break;
    case 4: if (event.value === 1) { ws.send("leftBumper"); console.log("Left Bumper"); } break;
    case 5: if (event.value === 1) { ws.send("rightBumper"); console.log("Right Bumper"); } break;
    case 12: // D-Pad Up = Boost
      if (event.value === 1 && !boostPressed) {
        boostPressed = true;
        ws.send("boost"); console.log("boost+1");
        setTimeout(() => boostPressed = false, cooldownTime);
      }
      break;
    case 14: // D-Pad Down = Boost Decrease
      if (event.value === 1 && !boostDecreasePressed) {
        boostDecreasePressed = true;
        ws.send("boostDecrease"); console.log("boost-1");
        setTimeout(() => boostDecreasePressed = false, cooldownTime);
      }
      break;
    default:
      break;
  }
});
