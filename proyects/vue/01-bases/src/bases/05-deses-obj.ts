interface Hero{
    name:string;
    age:number;
    codeName:string;
    power?:string //con el simbolo de interrogacion puede ser opcional en la
    //definicion del objeto
}

export const person: Hero = {
    name: 'Tony',
    age: 45,
    codeName: 'IronMan',
}

//desestructurando el objeto
const {age, name, power = `No tiene poder`} = person;

console.log({age, name,power})

//al crear un objeto args:any permite recibir todos y si no obtiene nada los dejara como undefined
interface CreateHeroArgs{
    name:string;
    age:number;
    codeName:string;
    power?:string
}
const createHero = ({name, age, codeName , power}:CreateHeroArgs) => ({
    id: 123456,
    name: name,
    age: age,
    codeName: codeName,
    power: power ?? 'No tiene poder' //el doble ?? permite preguntar si el valor es nulo 
    //o no valido imprima lo que sigue

})

console.log(createHero(person));