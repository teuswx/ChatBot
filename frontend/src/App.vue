<template>
  <div class="app">
    <h1>Fúria Chatbot</h1>
    <ChatBot />
  </div>
</template>

<script setup>
import ChatBot from './components/ChatBot.vue'
</script>

<style scoped>
h1{
  color: #39246d;
  
}
.app {
  max-width: 600px;
  margin: 2rem auto;
  padding: 1rem;
  background-color: #f6efef;
  color: #fff;
  border-radius: 12px;
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.3);
  font-family: 'Segoe UI', sans-serif;
  text-align: center;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2), 0 6px 20px 0 rgba(0, 0, 0, 0.19);
}
</style>
