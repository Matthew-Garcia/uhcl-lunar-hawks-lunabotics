// Save this as list_hid.js
const HID = require('node-hid');

const devices = HID.devices();
console.log(devices);

