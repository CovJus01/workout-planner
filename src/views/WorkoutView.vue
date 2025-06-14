<script setup lang="ts">
import DashboardWorkouts from "../components/Dashboard/DashboardWorkouts.vue"
import type Workout from "../types/workout.ts"
import Exercise from "../components/Workout/Exercise.vue"
const props = defineProps<{
  workout?: Workout
}>()

const workout = props.workout ?? {
  id: "ABC123",
  name: "NullWorkout",
  time: 42,
  exercises: [
  {
    name: "Bench Press",
    sets: 5,
    reps: 8,
    weight: 100,
  },
  {
    name: "Squat",
    sets: 5,
    reps: 8,
    weight: 160
  },
  ],
}
</script>

<template>
  <h1>{{workout.name}}</h1>
  <hr>
  <Exercise v-for="e in workout.exercises" :exercise="e"/>
</template>


<style scoped>
hr {
  border: 2px solid var(--light-onyx);
}
</style>
