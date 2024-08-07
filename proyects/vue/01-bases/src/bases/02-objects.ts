export const person = {
    lastName: 'stark',
    age: 45,
    address: {
        city: 'New York',
        zip: 51323,
        lat: 14.2323,
        lng: 34.5667
    }
};//as const;
//si se coloca as const; al final el objeto se vuelve solo de  lectura

//const person2 = person
//person2.lastName = 'fabrizioli'
//el problema de esto es que es paso por referencia no valor, haciendo que no permita cambiar los objetos sin modificar el primero
//ej cambio person2 pero modifica igualmente person 1
//se puede usar structuredClone que clona o hace paso por valor

const person2 = structuredClone(person)
person2.lastName = 'fabrizioli'
person2.address.city = 'LA'
console.log({person})
console.log({person2})

//al final se vuelve objeto export const para volverlo modulo y poderlo usar en otros lugares