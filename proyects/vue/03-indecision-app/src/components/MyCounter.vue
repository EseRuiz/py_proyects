<template>
  <section>
    <h3>Counter: {{ counter }}</h3>
    <h3>Square: {{ squareCounter }}</h3>

    <div>
      <button class="btn" @click="plusNum">+1</button>
      <button class="btnless" @click="lessNum">-1</button>
      <!-- <button @click="counter++">+1</button>
        <button @click="counter--">-1</button> -->
    </div>
  </section>
</template>

<script lang="ts" setup>
import { useCounter } from '@/composables/useCounter';

const props = defineProps({
  value: { type: Number, required: true }
});

const { counter, squareCounter } = useCounter(props.value);
// import { computed, ref } from 'vue';

//formas de hacerlo
// const props = defineProps<{
//     value:number;
// }>()
//con interfaces
// interface Props {
//   value: number;
// }
// const props = defineProps<Props>();

// const counter = ref(props.value);
// const squareCounter = computed(() => counter.value * counter.value);

const plusNum = () => {
  counter.value = counter.value + 1;
};
const lessNum = () => {
  counter.value = counter.value - 1;
};
</script>

<!-- scoped hace que el estilo solo afecte a los elementos del componente especifico en este caso Appvue -->
<!-- <style scoped>
  h1{
      color: rgb(255, 0, 98);
  }
  </style> -->
<style scope>
.btn {
  @apply p-5 bg-blue-500 rounded hover:bg-blue-700 mr-2;
}
.btnless {
  @apply p-5 bg-red-500 rounded hover:bg-red-700 mr-2;
}
</style>
