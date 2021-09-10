let a = prompt("Введите значение: ");
a++;
let check = (typeof a=="number") ? true:false;
if (check==true){
	a%=2
	if (a === 0){
		alert('Число чётное')
	}
	else{
		alert('Число нечётное')
	}
}
else{
	alert('Упс, кажется, вы ошиблись')
}