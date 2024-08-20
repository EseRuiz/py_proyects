<template>
  <div class="flex-1 overflow-y-auto p-4">
    <div class="flex flex-col space-y-2">
      <!-- Messages go here -->
      <ChatBubble :its-mine="true" :message="'Hola mundo'"></ChatBubble>
      <ChatBubble :its-mine="false" :message="'no'" image="https://yesno.wtf/assets/no/29-6bf57c5bf3fed2dcdbed64afff7a7930.gif" ></ChatBubble>
    </div>
  </div>
</template>

<script setup lang="ts">
import ChatBubble from './ChatBubble.vue';
</script>
