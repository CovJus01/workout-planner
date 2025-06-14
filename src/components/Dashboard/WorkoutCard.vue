<script setup lang="ts">
import AppCard from "../App/AppCard.vue"

defineProps<{
  workoutTitle: string
}>()
</script>

<template>
  <AppCard>
    <h3 class="oswald-light"> {{workoutTitle}} </h3>
    <slot></slot>
  </AppCard>
</template>

<style scoped>
h3 {
  margin-bottom: 10px;
}
</style>
