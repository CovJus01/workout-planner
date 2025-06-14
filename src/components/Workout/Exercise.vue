<script setup lang="ts">
  import type Exercise from "../../types/workout.ts"
  import Set from "./Set.vue"

const props = defineProps<{
  exercise: Exercise
  }>()


</script>

<template>
  <h2>{{exercise.name}}</h2>
  <Set v-for="i in exercise.sets" :index="i" />
</template>

<style scope>

h2 {
  margin-top: 1vh;
}

p {
  font-size: 1.5rem;
}
</style>
