<script setup lang="ts">
  import AppCard from "../App/AppCard.vue"
defineProps<{
  index: number
  }>()


</script>

<template>
  <AppCard>
    <div class="flex-container">

      <div class="flex-item title">
        <p>Set {{index}}</p>
      </div>

      <div class="flex-item input">
        <label >
          Reps
        </label>
        <input name="reps" type="number">
      </div>


      <div class="flex-item input">
        <label>
          Weight
        </label>
        <input name="weight" type="number">
      </div>

    </div>
  </AppCard>
</template>

<style scope>
.flex-container {
  display: flex;
  flex-wrap: wrap;
  gap: 10px;

  justify-content: start;
}
.flex-item {
  display:flex;
  align-items: center;
}

.title {
  width: 100%;
  color: var(--white-mute);
  font-weight: 700;
}
.input {

  padding-left: 20px;
  width: 35%;
}

label {
  font-size: 1.2rem;
  color: var(--light-indigo);
  font-weight: 700;
}

input {
  text-align: center;
  background-color: var(--dark-onyx);
  color: var(--white-mute);
  margin-left: 15px;
  border: var(--aquamarine) solid 2px;
  height: 2rem;
  width: 4rem;
  border-radius: 25%;
}
</style>
