<script setup lang="ts">
import { RouterView } from 'vue-router'
import AppHeader from './components/App/AppHeader.vue'
</script>

<template>
  <header>
    <AppHeader/>
  </header>
  <main>
    <RouterView/>
  </main>


</template>

<style scoped>
</style>
