<script setup>
import WorkoutTable from "../components/WorkoutTable.vue";
const emit = defineEmits(["updatePage"]);

function updatePage() {
  emit("updatePage", "Workout");
}
</script>

<template>
  <h2>Start a workout</h2>
  <WorkoutTable @click="updatePage" />
</template>

<style scoped>
h2 {
  padding: 5px;
}
</style>
