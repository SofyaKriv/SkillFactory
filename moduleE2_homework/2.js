let a = prompt("Введите значение: ");
let type = typeof a;
switch (type){
	case "number":
		alert(a + " - число")
	case "string":
		alert(a + " - строка")
	case "boolean":
		alert(a + " - логический")
}