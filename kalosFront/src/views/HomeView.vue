<script setup>
import sectionAccess from "../components/sectionAccess.vue";
</script>

<template>
  <main>
    <sectionAccess
      title="Datos Físicos"
      desc = "Toma nota de tus datos físicos como peso y medidas. ¡Estas medidas son la base del conocimiento sobre ti mismo!"
      link = "/dataIn"/>

      <sectionAccess
      title="Alimentación"
      desc = "Somos lo que comemos. ¿Cuanto comes? ¿Cuando? ¿Qué comes? ¿Cómo te afecta? Dependiendo de tus objetivos y estado
    actual, la alimentación puede significar el 85% de tus logros!"
      link = ""/>

      <sectionAccess
      title="Ejercicio Físico"
      desc = "¿Entrenas para estar fuerte? ¿Para perder peso? ¿Por salud mental? Sea cual sea el motivo, la monitorización de
    tu actividad física te llevará a mejoras y una sensación de progreso más palpable."
      link = ""/>

      <sectionAccess
      title="Hábitos"
      desc = "Monitorizar tus hábitos puede ayudarte a comprender como y porqué tus datos físicos fluctuan, además de revelar
   patrones que tu mismo no conocías."
      link = ""/>

      <sectionAccess
      title="Colabora con nosotros"
      desc = "Cualquier donación es bienvenida. Las API de alimentación y Google, además del despliegue en la nube de la
    aplicación, no son gratuitas. Sin embargo, ¡Kalos App siempre lo será para ti!"
      link = "/about"/>
  </main>
</template>
