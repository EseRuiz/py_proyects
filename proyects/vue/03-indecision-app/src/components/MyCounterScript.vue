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

<script lang="ts">
import { computed, defineComponent, ref } from 'vue';
import { useCounter } from '@/composables/useCounter';

export default defineComponent({
  props: {
    value: {type: Number, required: true},
  },
  setup(props) {
    const { counter, squareCounter } = useCounter(props.value);

    return {
      counter,
      squareCounter
    };
  }
});

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
