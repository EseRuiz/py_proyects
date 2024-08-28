import { expect, test } from 'vitest';
import { addArray, sum } from '../../src/helpers/sum';
import { describe } from 'node:test';

describe('add function', () => {
  test('adds 1 + 2 to equal 3', () => {
    //   if (sum(1, 2) !== 3) {
    //     throw new Error('La suma no es correcta');
    //   }
    //preparacion
    const a = 1;
    const b = 4;
    //accion
    const result = sum(a, b);
    //el resultado esperado
    expect(result).toBe(a + b);
  });
});

describe('addArray  function', () => {
  test('Deberia retornar 0 si el arreglo es vacio', () => {
    const numberArray = [];
    const result = addArray(numberArray);

    expect(result).toBe(0);
  });

  test('Deberia retornar el valor adecuado de la suma del arreglo', () => {
    const numberArray = [1, 2, 3, 4, 5];
    const result = addArray(numberArray);

    expect(result).toBe(15);
  });
});
