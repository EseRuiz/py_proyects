//desestructuracion con arreglos
const sayayin = ['Goku', 'Vegueta', 'Trunks', 'Goten']

//const [g] = sayayin
//desesctructurar arreglos es posicional osea se deben ir ubicando uno a uno
//si quisiera el segundo valor de arreglo puedo usar una , asi :
const [,v,g] = sayayin
//de esta forma la primera variable se deja vacia y puedo tomar la siguiente
//si los quiero todos
//const [g,v,t,g] = sayayin
console.log({v,g});
//
const returnArray = () => {
    return [123, 'ABC'] as const;
}
//al ser una funcion que retorna un arreglo, si no se coloca como 'as const'
//define cada argumento del arreglo como posible number/string/object o lo que contenga
//para evitar eso y que cada argumento tenga siempre su valor se deja como as const
//desestructurando 
const [ number, letters] = returnArray();

console.log(number * 2, letters.toLowerCase())