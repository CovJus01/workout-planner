<script setup lang="ts">
</script>
<template>
  <div class="card-container">
    <slot></slot>
  </div>
</template>

<style scoped>
.card-container {
  margin: 0.5em;
  padding: 10px;
  border-radius: 12px;
  background-color: var(--onyx)
}
</style>
