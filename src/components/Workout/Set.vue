<script setup lang="ts">

defineProps<{
  index: number
  }>()


</script>

<template>
  <p>Set {{index}}:</p>
  <label for="reps">
    Reps:
  </label>
  <input name="reps">
  <label for="weight">
    Weight:
  </label>
  <input name="weight">
</template>

<style scope>

</style>
