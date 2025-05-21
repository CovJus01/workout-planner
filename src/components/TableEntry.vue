<script setup>
defineProps({
  name: {
    type: String,
    required: true,
  },
  description: {
    type: String,
    required: false,
  },
  duration: {
    type: Number,
    required: false,
  },
});
</script>

<template>
  <div id="WorkoutTable">
    <h3>{{ name }}</h3>
    <p>{{ description + " " + duration + "min" }}</p>
  </div>
</template>

<style scoped>
div {
  border-radius: 5px;
  background-color: #333333;
  margin-bottom: 5px;
}

h3 {
  padding-left: 5px;
}

p {
  padding-left: 5px;
}
</style>
