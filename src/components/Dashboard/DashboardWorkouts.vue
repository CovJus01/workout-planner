<script setup lang="ts">
import WorkoutCard from "./WorkoutCard.vue"
import {useRouter} from 'vue-router'

const router = useRouter()

function handleClickWorkout() {
  router.push("/workout")

}
</script>
<template>
  <WorkoutCard workout-title="Workout 1" @click="handleClickWorkout">
    <p>32min 10 exercises</p>
  </WorkoutCard>
</template>
