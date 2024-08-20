<!-- Fuente: https://tailwindcomponents.com/component/chat-layout -->
<template>
  <div class="bg-gray-100 h-screen flex flex-col max-w-lg mx-auto">
    <div class="bg-blue-500 p-4 text-white flex justify-between items-center">
      <span>Mi esposa</span>
    </div>

    <!-- chat messages -->
    <ChatMessages></ChatMessages>

    <!-- MessageBox -->
    <MessageBox></MessageBox>

  </div>
</template>

<script setup lang="ts">
import ChatMessages from '@/components/my-counter-script/chat/ChatMessages.vue';
import MessageBox from '@/components/my-counter-script/chat/MessageBox.vue';
</script>
