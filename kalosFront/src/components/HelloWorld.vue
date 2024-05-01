<script setup>
defineProps({
  msg: {
    type: String,
    required: true
  }
})
</script>

<template>
  <div class="greetings">
    <h1 class="green">{{ msg }}</h1>
    <h3>
      Bienvenido. Este es un lugar donde controlar tu peso, tus hábitos y cualquier número relacionado con tu vida.
    </h3>
  </div>
</template>

