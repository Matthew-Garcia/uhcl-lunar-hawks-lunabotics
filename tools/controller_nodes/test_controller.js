// Save as test_controller.js
const DualShock = require('dualshock');

const controller = DualShock({
  type: 'ds4', // 'ds4' for PS4 or PS5 controllers
  smoothAnalog: true,
  smoothMotion: false,
  joyDeadband: 4,
  analogStickSmoothing: true
});

controller.on('connected', () => {
  console.log("Controller Connected!");
});

controller.on('left:move', (data) => {
  console.log("Left Stick: ", data);
});

controller.connect();
