let fruits = new Map([
	["apple", "green"],
	["strawberry", "red"],
	["blueberry", "blue"]
]);
for (let i of fruits.keys()){
	console.log(`Ключ - ${i}, значение - ${fruits.get(i)}`);
}