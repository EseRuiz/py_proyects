import { computed, ref } from 'vue';

export const useCounter= (initialValue: number ) => {
    const counter = ref(initialValue);
    //const squareCounter = computed(() => counter.value * counter.value);
    const squareCounter = computed(() => counter.value * counter.value);
    return{
        counter,


        //read-only
        squareCounter
    }

}