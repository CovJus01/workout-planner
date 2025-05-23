<script setup>
import Exercise from "../components/Exercise.vue";
defineProps({
  workoutName: {
    type: String,
    required: false,
  },
});
</script>

<template>
  <h2>{Workout Name}</h2>
  <Exercise />
</template>

<style scoped>
h2 {
  padding: 5px;
}
</style>
