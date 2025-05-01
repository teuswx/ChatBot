<template>
  <div class="chat-container">
    <div class="messages">
      <div class="background"></div> <!-- background separado -->
      
      <div
        v-for="(msg, index) in mensagens"
        :key="index"
        :class="msg.tipo"
        class="message"
      >
        <div v-html="formatarMensagem(msg.texto)"></div>
      </div>
    </div>
    <input class="envio"
      v-model="mensagem"
      @keyup.enter="enviarMensagem"
      placeholder="Digite sua mensagem..."
    />
    <button @click="enviarMensagem">Enviar</button>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import axios from 'axios'

const mensagens = ref([])
const mensagem = ref('')

const enviarMensagem = async () => {
  if (mensagem.value.trim() === '') return

  mensagens.value.push({ texto: mensagem.value, tipo: 'usuario' })

  try {
    const response = await axios.post('http://localhost:8000/chat', {
      texto: mensagem.value
    })
    console.log(response.data.resposta)
    mensagens.value.push({ texto: response.data.resposta, tipo: 'bot' })
  } catch (error) {
    mensagens.value.push({ texto: 'Erro ao obter resposta do servidor.', tipo: 'bot' })
  }

  mensagem.value = ''
}

const formatarMensagem = (texto) => {
  return texto.replace(/\n/g, '<br>')
}
</script>

<style scoped>
.chat-container {
  display: flex;
  flex-direction: column;
  width: 400px;
  margin: 20px auto;
  border: 1px solid #ccc;
  border-radius: 5px;
  padding: 10px;
  background-color: #eae2e2;
}

button {
  margin-top: 10px;
  background-color: #39246d;
  color: white;
  border: none;
  padding: 8px 16px;
  border-radius: 5px;
  cursor: pointer;
}

button:hover {
  background-color: #825ce0;
}

.envio {
  height: 30px;
  border-radius: 8px;
  border: none;
  background: rgb(255, 255, 255);
  padding: 10px;
  color: black;
  outline: none;
}

.messages {
  position: relative;
  display: flex;
  flex-direction: column;
  height: 300px;
  overflow-y: auto;
  margin-bottom: 10px;

  border-radius: 5px;
}


.background {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background-image: url('Furia_Esports_logo.png');
  background-size: 300px 300px;
  background-position: center;
  background-repeat: no-repeat;
  opacity: 0.2; 
  z-index: 0;
}


.message {
  position: relative;
  z-index: 1;
  display: flex;
  margin: 5px 0;
  padding: 5px 10px;
  border-radius: 10px;
  max-width: 80%;
  word-wrap: break-word;
}

.usuario {
  align-self: flex-end;
  background-color: #39246d;
  color: white;
}

.bot {
  align-self: flex-start;
  background-color: #5975a7;
  color: white;
}
</style>
