function simpleCheck(n){
	let k = false;
	if (n==0 || n==1){
		k = true;
	}
	for (let i=2; i<n; i++){
		if (n%i==0){
			k = true;
		}
	}
	return k;
}
let a = prompt("Введите значение: ");
if (simpleCheck(a) == false){
	console.log("Число простое");
}
else{
	console.log("Число сложное");
}