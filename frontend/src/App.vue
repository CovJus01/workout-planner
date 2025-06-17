<script setup lang="ts">
import { RouterView } from 'vue-router'
import AppHeader from './components/App/AppHeader.vue'
import AppFooter from './components/App/AppFooter.vue'
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
  <footer>
    <AppFooter />
  </footer>


</template>
<style scoped>
.view-container {
  margin-left: 3vw;
  margin-right: 3vw;
}
</style>
