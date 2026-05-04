const WebSocket = require('ws');
const HID = require('node-hid');


const vendorId = 0x2E95; // Razer USA, Ltd
const productId = 0x7725; // Razer Wolverine V3 Pro for Xbox

//const vendorId = 0x045E; // Xbox controller
//const productId = 0x0B13;

const ws = new WebSocket('ws://192.168.0.168:81');

let isConnected = false;

// Debounce + Edge Detection
let lastBoost = 0;
let lastBoostDecrease = 0;
let boostPressed = false;
let boostDecreasePressed = false;
let cooldownTime = 500;

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

const device = new HID.HID(vendorId, productId);
console.log("Controller Connected!");

device.on("data", (data) => {
  const leftStickY = data[4];
  const rightStickX = data[6];
  const aButton = data[14];
  const rTrigger = data[11];
  const lTrigger = data[9];
  const triangle = data[14];
  const boost = data[13];
  const boostDecrease = data[13];
  const rightBumper = data[14];
  const leftBumper = data[14];

  // Current frame status
  let commandSent = false;

  if (isConnected) {
    // Movement
    if (leftStickY < 100) {
      if (rightStickX < 100) {
        ws.send("FWDL"); console.log("Forward Left");
      } else if (rightStickX > 150) {
        ws.send("FWDR"); console.log("Forward Right");
      } else {
        ws.send("FWD"); console.log("Forward");
      }
      commandSent = true;
    }
    else if (leftStickY > 150) {
      if (rightStickX < 100) {
        ws.send("BCKL"); console.log("Back Left");
      } else if (rightStickX > 150) {
        ws.send("BCKR"); console.log("Back Right");
      } else {
        ws.send("BACK"); console.log("Backward");
      }
      commandSent = true;
    }

    // Triggers
    else if (rTrigger === 255) {
      ws.send("up"); console.log("Right Trigger");
      commandSent = true;
    }
    else if (lTrigger === 255) {
      ws.send("down"); console.log("Left Trigger");
      commandSent = true;
    }

    // Buttons
    else if (aButton === 1) {
      ws.send("X"); console.log("Excavator");
      commandSent = true;
    }
    else if (triangle === 16) {
      ws.send("Y"); console.log("Dump");
      commandSent = true;
    }
    else if (rightBumper === 128) {
      ws.send("rightBumper"); console.log("right Bumper");
      commandSent = true;
    }
    else if (leftBumper === 64) {
      ws.send("leftBumper"); console.log("left Bumper");
      commandSent = true;
    }

    // Boost (D-Pad Up → boost+1)
    const currentBoost = boost;
    if (currentBoost === 1 && lastBoost === 0 && !boostPressed) {
      boostPressed = true;
      ws.send("boost"); console.log("boost+1");
      commandSent = true;
      setTimeout(() => { boostPressed = false; }, cooldownTime);
    }

    // Boost Decrease (D-Pad Down → boost-1)
    const currentBoostDecrease = boostDecrease;
    if (currentBoostDecrease === 5 && lastBoostDecrease === 0 && !boostDecreasePressed) {
      boostDecreasePressed = true;
      ws.send("boostDecrease"); console.log("boost-1");
      commandSent = true;
      setTimeout(() => { boostDecreasePressed = false; }, cooldownTime);
    }

    // Update last state
    lastBoost = currentBoost;
    lastBoostDecrease = currentBoostDecrease;

    // If no other command sent
    if (!commandSent) {
      ws.send("STOP");
      console.log("Stop");
    }
  } else {
    console.log("WebSocket not connected yet.");
  }
});
