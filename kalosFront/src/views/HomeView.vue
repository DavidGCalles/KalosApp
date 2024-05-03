<script setup>
import Card from 'primevue/card';

</script>

<template>
  <main>
    <div class="cards-container">
      <Card style="text-align: center;">
        <template #header><i class="pi pi-user" style="font-size: 5rem"></i></template>
        <template #title><RouterLink to="/dataIn">Datos Físicos</RouterLink></template>
        <template #content>
          <p>Toma nota de tus datos físicos como peso y medidas. ¡Estas medidas son la base del conocimiento sobre ti mismo!</p>
        </template>
      </Card>

      <Card style="text-align: center;">
        <template #header><i class="pi pi-user" style="font-size: 5rem"></i></template>
        <template #title><RouterLink to="">Alimentación</RouterLink></template>
        <template #content>
          <p>Somos lo que comemos. ¿Cuanto comes? ¿Cuando? ¿Qué comes? ¿Cómo te afecta? Dependiendo de tus objetivos y estado
      actual, la alimentación puede significar el 85% de tus logros!</p>
        </template>
      </Card>

      <Card style="text-align: center;">
        <template #header><i class="pi pi-user" style="font-size: 5rem"></i></template>
        <template #title><RouterLink to="">Hábitos</RouterLink></template>
        <template #content>
          <p>Monitorizar tus hábitos puede ayudarte a comprender como y porqué tus datos físicos fluctuan, además de revelar
    patrones que tu mismo no conocías.</p>
        </template>
      </Card>

      <Card style="text-align: center;">
        <template #header><i class="pi pi-user" style="font-size: 5rem"></i></template>
        <template #title><RouterLink to="/about">Colabora con nosotros</RouterLink></template>
        <template #content>
          <p>Cualquier donación es bienvenida. Las API de alimentación y Google, además del despliegue en la nube de la
      aplicación, no son gratuitas. Sin embargo, ¡Kalos App siempre lo será para ti!</p>
        </template>
      </Card>
    </div>
  </main>
</template>

<style>
.cards-container {
  display: flex;
  clear: both;
  justify-content: center; 
  align-items: center;     
  gap: 20px;
}
</style>
