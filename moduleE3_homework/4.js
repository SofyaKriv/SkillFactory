function show(i){
	console.log(i)
}

let a = prompt("Введите первое значение: ");
let b = prompt("Введите второе значение: ");
for (let i=a; i<=b; i++){
	setInterval(show(i), 1000);
}