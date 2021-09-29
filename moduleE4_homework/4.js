powerArray = new Array();

function ElectricalDevice(name, power){
  this.name = name, 
  this.power = power
}

ElectricalDevice.prototype.getTurnOn = function(command){
  if (command == 'On'){
    powerArray.push(this)
  }
  else{
    powerArray.slice(powerArray.indexOf(this), 1)
  }
  console.log(Object.getPrototypeOf(this).power),
  console.log(`The device is turned ${command}`)
}

function ConsumedPower(powerArray){
  sumPower = 0;
  powerArray.forEach((i) => {sumPower += i.power});
  return sumPower
}

function Lamp(name, color, power){
  this.name = name,
  this.color = color,
  this.power = power
}

function Computer(name, power){
  this.name = name,
  this.power = power
}

Lamp.prototype = new ElectricalDevice()
Computer.prototype = new ElectricalDevice()

const tableLamp = new Lamp('Table Lamp', 'blue', 60);
const computer = new Computer('NewComp', 220);

tableLamp.getTurnOn('On');
computer.getTurnOn('On')

console.log(powerArray)
console.log(ConsumedPower(powerArray))