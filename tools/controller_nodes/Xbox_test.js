// Save this as ps5_test.js
const HID = require('node-hid');

// Update with your vendorId and productId from the previous step
const vendorId = 0x045E; 
const productId = 0x0B13;

const device = new HID.HID(vendorId, productId);

console.log("Controller Connected!");

device.on("data", (data) => {
  console.log("Data received: ", data);
});

device.on("error", (err) => {
  console.error("Error: ", err);
});

