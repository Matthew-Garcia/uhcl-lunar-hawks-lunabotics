const HID = require('node-hid');

// Replace these with your actual vendorId and productId
const vendorId = 0x045E; // Sony
const productId = 0x0B13; // DualSense (PS5 Controller)

const device = new HID.HID(vendorId, productId);

console.log("🎮 Controller Connected!");

// Event Listener for Joystick Data
device.on("data", (data) => {
  // Read Joystick values
  const leftStickX = data[2];  // Left Stick X-axis
  const leftStickY = data[4];  // Left Stick Y-axis
  const rightStickX = data[6]; // Right Stick X-axis
  const rightStickY = data[8]; // Right Stick Y-axis

  // Print the values
  console.clear();
  console.log("🎮 Joystick Values:");
  console.log(`Left Stick X: ${leftStickX} | Y: ${leftStickY}`);
  console.log(`Right Stick X: ${rightStickX} | Y: ${rightStickY}`);
});

