

// console.log('Inicio');

import type { Hero } from "../data/heroes";
import { getHeroById } from "./07-imp-exp";

// new Promise((resolve, reject) => {
//     //console.log('Cuerpo de la promesa');
//     setTimeout(() => {
//         //resolve('Cumplio')
//         reject('No cumplio')
//     }, 1000);
// }).then((message) => console.log(message))
//   .catch(erroMessage =>  console.log(erroMessage))
//   .finally(() => console.log('Fin de la promesa'))


// console.log('final');

const getHeroByIdAzync = (id: number):Promise<Hero> => {
    return new Promise((resolve,reject) => {
        setTimeout(()=>{
            const hero = getHeroById( id );

            // if ( hero ){
            //     resolve(hero);
                
            // } else {
            //     reject(`Heroe no encontrado #${id}`)
            // }
            //resumiendo con operador ternario
            hero ? resolve(hero): reject(`Heroe no encontrado #${id}`);
        }, 1500);
    })
}

getHeroByIdAzync(2)
    .then(hero => console.log('El nombre es', hero.name))
    .catch(erroMessage => alert(erroMessage))
