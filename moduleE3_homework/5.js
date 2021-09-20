let a = prompt("Введите значение: ");
let b = prompt("Введите степень: ");
let res = (x, n) => {
	let deg = 1;
	for (let i=0; i<n; i++){
		deg*=x;
	}
	console.log(deg);
};
res(a, b);