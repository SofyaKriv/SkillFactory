powerArray = new Array();

class ElectricalDevice{
  constructor(name, power){
    this.name = name; 
    this.power = power;
  }
  getTurnOn(command){
    if (command == 'On'){
      powerArray.push(this)
    }
    else{
      powerArray.slice(powerArray.indexOf(this), 1)
    }
    console.log(Object.getPrototypeOf(this).power),
    console.log(`The device is turned ${command}`)
  }
}

function ConsumedPower(powerArray){
  sumPower = 0;
  powerArray.forEach((i) => {sumPower += i.power});
  return sumPower
}

class Lamp extends ElectricalDevice{
  constructor(name, power, color){
    super(name, power);
    this.color = color;
  }
}

class Computer extends ElectricalDevice{
  constructor(name, power, type){
    super(name, power);
    this.type = type;
  }
}

Computer.prototype = new ElectricalDevice()

let tableLamp = new Lamp('Table Lamp', 60, 'blue');
const computer = new Computer('NewComp', 220, 'LP');

tableLamp.getTurnOn('On');
computer.getTurnOn('On')

console.log(powerArray)
console.log(ConsumedPower(powerArray))