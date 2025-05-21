<script setup>
defineProps({
  text: {
    type: String,
    required: true,
  },
});
</script>

<template>
  <h1>{{ text }}</h1>
</template>

<style scoped>
h1 {
  display: block;
}
</style>
