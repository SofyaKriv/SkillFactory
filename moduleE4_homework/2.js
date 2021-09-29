function func(str, obj){
	return obj.hasOwnProperty(str);
};

let user = {     
	name: "John",  
	age: 30        
};
line = 'name';
console.log(func(line, user));
