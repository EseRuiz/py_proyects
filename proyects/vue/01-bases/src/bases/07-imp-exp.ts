import heroes, { type Owner } from "../data/heroes";

export const getHeroById = (id: number) =>{
    return heroes.find(hero => hero.id === id) //?? {}
}

console.log( getHeroById(100));

//regresar todos los heroes basados en una casa

export const getHeroesByOwner = (owner:Owner) => {
    return heroes.filter(hero => hero.owner === owner) ?? {}
}

console.log(getHeroesByOwner('Marvel'))