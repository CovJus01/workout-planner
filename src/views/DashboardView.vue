<script setup lang="ts">
import WorkoutCard from "../components/Dashboard/WorkoutCard.vue"
</script>

<template>
  <h2>
    Start
  </h2>
  <WorkoutCard workout-title="Workout 1">
    <p>32min 10 exercises</p>
  </WorkoutCard>
  <h2>
    Stats
  </h2>
  <AppCard>
   Graph 1
  </AppCard>
  <h2>
    Build
  </h2>
  <AppCard>
    Edit existing
  </AppCard>
  <AppCard>
    + Add new
  </AppCard>

</template>


<style scoped></style>
