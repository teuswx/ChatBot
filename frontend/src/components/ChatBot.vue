<template>
  <div class="chat-container">
    <div class="messages">
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

button{
  margin-top: 10px;
  background-color: #39246d;
}

button:hover{
  background-color: #825ce0;
}
.envio{
  height: 30px;
  border-radius: 8px;
  border: none;
  background: rgb(255, 255, 255);
  padding: 10px;
  color: black;
  outline: none;

}


.messages {
  display: flex;
  flex-direction: column;
  height: 300px;
  overflow-y: auto;
  margin-bottom: 10px;
}

.message {
  display: flex;
  margin: 5px 0;
  padding: 5px 10px;
  border-radius: 10px;
  max-width: 80%;
}


.usuario {
  align-self: flex-end;
  background-color: #39246d;
}


.bot {
  align-self: flex-start;
  background-color: #5975a7;
}
</style>
