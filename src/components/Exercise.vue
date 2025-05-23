<script setup>
defineProps({
  exerciseName: {
    type: String,
    required: false,
  },
  exerciseSets: {
    type: Number,
    required: false,
  },
  exerciseReps: {
    type: Number,
    required: false,
  },
});
</script>

<template>
  <h3>{Exercise Name}</h3>
  <h4>{{ exerciseSets + "x" + exerciseReps }}</h4>
  <div>
    <h4>Last</h4>
    <p>Set 1: 8x65lbs</p>
  </div>
  <br />
  <div>
    <h4>Set 1:</h4>
    <label>Weight =</label>
    <input type="text-area" />
    <br />
    <label>Reps =</label>
    <input type="text-area" />
  </div>
</template>

<style scoped>
h3 {
  padding: 5px;
}
</style>
