<script setup>
import WelcomeItem from './WelcomeItem.vue'
import DocumentationIcon from './icons/IconDocumentation.vue'
import ToolingIcon from './icons/IconTooling.vue'
import EcosystemIcon from './icons/IconEcosystem.vue'
import CommunityIcon from './icons/IconCommunity.vue'
import SupportIcon from './icons/IconSupport.vue'
</script>

<template>
  <WelcomeItem>
    <template #icon>
      <DocumentationIcon />
    </template>
    <template #heading>Datos Físicos</template>

    Toma nota de tus datos físicos como peso y medidas. ¡Estas medidas son la base del conocimiento sobre ti mismo!
  </WelcomeItem>

  <WelcomeItem>
    <template #icon>
      <EcosystemIcon />
    </template>
    <template #heading>Alimentación</template>

    Somos lo que comemos. ¿Cuanto comes? ¿Cuando? ¿Qué comes? ¿Cómo te afecta? Dependiendo de tus objetivos y estado
    actual, la alimentación puede significar el 85% de tus logros.
  </WelcomeItem>

  <WelcomeItem>
    <template #icon>
      <CommunityIcon />
    </template>
    <template #heading>Ejercicio Físico</template>

    ¿Entrenas para estar fuerte? ¿Para perder peso? ¿Por salud mental? Sea cual sea el motivo, la monitorización de
    tu actividad física te llevará a mejoras y una sensación de progreso más palpable.
  </WelcomeItem>

  <WelcomeItem>
    <template #icon>
      <ToolingIcon />
    </template>
    <template #heading>Hábitos</template>

   Monitorizar tus hábitos puede ayudarte a comprender como y porqué tus datos físicos fluctuan, además de revelar
   patrones que tu mismo no conocías.
  </WelcomeItem>

  <WelcomeItem>
    <template #icon>
      <RouterLink to="/about"><SupportIcon /></RouterLink>
    </template>
    <template #heading>Colabora con nosotros</template>

    Cualquier donación es bienvenida. Las API de alimentación y Google, además del despliegue en la nube de la
    aplicación, no son gratuitas. Sin embargo, ¡Kalos App siempre lo será para ti!
  </WelcomeItem>
</template>
