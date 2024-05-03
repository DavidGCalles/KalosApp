<script setup>
import {RouterView } from 'vue-router'
import headerNav from "./components/headerNav.vue"
</script>

<template>
  <header>
    <headerNav/>
  </header>

  <RouterView />
</template>