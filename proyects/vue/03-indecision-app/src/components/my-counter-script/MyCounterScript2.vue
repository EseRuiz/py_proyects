<template>
  <section>
    <h3>Counter: {{ counter }}</h3>
    <h3>Square: {{ squareCounter }}</h3>

    <div>
      <button @click="counter++">+1</button>
      <button @click="counter--">-1</button>
      <!-- <button @click="counter++">+1</button>
        <button @click="counter--">-1</button> -->
    </div>
  </section>
</template>

<script lang="ts" src="./MyCounterScript2">


//con interfaces
// interface Props {
//   value: number;
// }
// const props = defineProps<Props>();

// const counter = ref(props.value);
// const squareCounter = computed(() => counter.value * counter.value);

// const plusNum = () => {
//   counter.value = counter.value + 1;
// };
// const lessNum = () => {
//   counter.value = counter.value - 1;
// };
</script>

<!-- scoped hace que el estilo solo afecte a los elementos del componente especifico en este caso Appvue -->
<!-- <style scoped>
  h1{
      color: rgb(255, 0, 98);
  }
  </style> -->
