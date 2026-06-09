<script setup lang="ts">
import AppHeader from '@/components/AppHeader.vue'
import AppFooter from '@/components/AppFooter.vue'
</script>

<template>
  <div class="app-container">
    <AppHeader />
    <div class="page-content">
      <RouterView />
    </div>
    <AppFooter />
  </div>
</template>

<style scoped>
.app-container {
  height: 100vh;
  display: flex;
  flex-direction: column;
}

.page-content {
  background-color: #1E2E2E;
  flex: 1 0 0;
}
</style>
