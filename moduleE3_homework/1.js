function funcCount(n){
	let k = n%2;
	if (k == 0 && n!=0){
		return "четное";
	}
	else if (n == 0){
		return "нуль";
	}
	else {
		return "нечетное";
	}
}
let a = [1,2,null,"-",5,0,6,8];
let chet = 0
let nechet = 0
let nul = 0
for (let i in a){
	if (typeof a[i]=="number"){
		if (funcCount(i) == "четное"){
			chet++;
		}
		else if (funcCount(i) == "нуль"){
			nul++;
		}
		else {
			nechet++;
		}
	}
}
console.log("Чётных элементов: " + chet)
console.log("Нечётных элементов: " + nechet)
console.log("Нулевых элементов: " + nul)