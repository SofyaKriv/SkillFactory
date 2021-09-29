function func(obj){
	for (let i in obj){
		console.log(`Ключ - ${i}, значение - ${obj[i]}`);
	}
};

let user = {     
	 name: "John",  
	 age: 30        
};

func(user);

