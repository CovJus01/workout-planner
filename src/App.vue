<script setup lang="ts">
import { RouterView } from 'vue-router'
import AppHeader from './components/App/AppHeader.vue'
</script>

<template>
  <header>
    <AppHeader/>
  </header>
  <main>
    <div class="view-container">
    <RouterView/>
    </div>
  </main>


</template>
<style scoped>
.view-container {
  margin-left: 3vw;
  margin-right: 3vw;
}
</style>
