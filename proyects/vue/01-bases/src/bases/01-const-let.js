//crear una variable siempre fija, constantes mas rapida mas ligeras
const firstName = 'Tony'
const lastName = 'Stark'

console.log({firstName, lastName});

//si quiero que se pueda cambiar let o var
let secondName = 'pepe'
secondName = 'fefe'

//template literal se define con las backtip comilla simple invertida ``
console.log(`${ firstName } ${  lastName }`);

//const fullName = `${ firstName } ${  lastName }`;

//console.log(fullName)

//export const definir la variable como modulo para que no sea  importado
export const fullName = `${ firstName } ${  lastName }`;