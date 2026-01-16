const HID = require('node-hid');

// Replace with your actual vendorId and productId
const vendorId = 0x045E; // Sony
const productId = 0x0B13; // DualSense (PS5 Controller)

const device = new HID.HID(vendorId, productId);

console.log("🎮 Controller Connected!");
console.log("Move the sticks or press buttons to see the raw data...");

device.on("data", (data) => {
  console.clear();
  console.log("🎮 RAW DATA:");
  
  // Display each byte
  for (let i = 0; i < data.length; i++) {
    console.log(`data[${i}] = ${data[i].toString(16).padStart(2, '0')} (${data[i]})`);
  }
});

