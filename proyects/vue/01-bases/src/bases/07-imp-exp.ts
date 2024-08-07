import heroes, { owners } from "../data/heroes";

export const getHeroById = (id: number) =>{
    return heroes.find(hero => hero.id === id) ?? {}
}

console.log( getHeroById(100));

//regresar todos los heroes basados en una casa

export const getHeroesByOwner = (owner:string) => {
    return heroes.filter(hero => hero.owner === owner) ?? {}
}
const [ d, m] = owners;
console.log(getHeroesByOwner(m))