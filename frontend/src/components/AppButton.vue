<script setup lang="ts">
</script>

<template>
  <div class="btn-container">
    <div class="btn-content">
      <slot>
        BTN
      </slot>
    </div>
  </div>
</template>


<style scoped>
.btn-container {
  --accent-color: #555;
  background-color: var(--accent-color);
  border: 0 solid #000;
  border-radius: 0.5rem;

  width: 3rem;
  height: 1.5rem;
  display: flex;
  justify-content: center;
  align-items: center;
  padding: 0.2rem;
}

.btn-content {
  color: #EAEAEA;
}
</style>
