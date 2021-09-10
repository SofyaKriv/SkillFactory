let a = [1,2,null,"-",5,0,6,8];
let chet = 0
let nechet = 0
let nul = 0
for (let i in a){
	if (typeof a[i]=="number"){
		let k = a[i]%2;
		if (k == 0 && a[i]!=0){
			chet++;
		}
		else if (a[i] == 0){
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