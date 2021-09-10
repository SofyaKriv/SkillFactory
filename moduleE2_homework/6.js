let a = [1,1,1,1,1,1,1,1];
k = a[0]
n = 0
for (let i in a){
	if (a[i]==k){
		n++;
		console.log(n);
	}
}
if (n == a.length){
	console.log("Массив состоит из одинаковых элементов")
}
else{
	console.log("Массив состоит из разных элементов")
}