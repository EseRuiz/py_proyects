/*function greetPerson(name: string){
    return `Hola, ${name}` ;
}*/

//con funcion de flecha con asignacion
/*const greetPerson= (name: string) => {
    return `Hola, ${ name }` ;
}*/

//resumiendo la funcion flecha
const greetPerson = (name: string) => `Hola, ${ name }` ;

console.log(greetPerson('Daniel'));
//funcion flecha
/*
const getUser = () => {
    return {
        uid: 'ABC-123',
        username: 'Tony001'
    }
}*/
//resumiendolo sin return siendo funcion flecha
const getUser = (uid:string) => ({
    uid: uid,
    username: 'Tony001'
});

console.log(getUser('XYZ-456'))

const heroes = [
    {
        id:1,
        name: 'Batman',
    },
    {
        id:2,
        name: 'Superman',
        power: 'Velocidad',
    },
]

//llamar un valor especifico del arreglo o objeto
const hero = heroes.find((h)=>h.id === 2);
//typescript captura el error con el ? permitiendo el funcionamiento nullcheck se llama , si no es nulo
//toma el nombre
console.log(hero?.power?.toUpperCase())