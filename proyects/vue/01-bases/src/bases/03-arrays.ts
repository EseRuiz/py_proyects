export const numberArray = [1,2,3,4,5];
//para hacerlo el arreglo de solo lectura se  puede hacer asi: const numberArray = [1,2,3,4,5] as const;
//asi no se podra agregar o modificar
//numberArray.push(number); inserta un numero en la lista
numberArray.push(6);

//operador spread '...' para hacer una copia por valor
//funciona por que no tiene sub arreglos, con sub arreglos se debe hacer spread '...' a todos

const numberArray2 = [... numberArray]
numberArray.push(7);

console.log({numberArray, numberArray2});
