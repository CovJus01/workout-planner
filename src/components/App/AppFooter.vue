<script setup lang="ts">
  import {RouterLink} from "vue-router"
</script>


<template>
  <div class="footer-container">
    <RouterLink to="/workouts">
      <h1 class ="oswald-bold">|||</h1>
    </RouterLink>
    <RouterLink to="/">
      <h1 class ="oswald-bold">+</h1>
    </RouterLink>
    <RouterLink to="/profile">
      <h1 class ="oswald-bold">(-_-)</h1>
    </RouterLink>
  </div>
</template>

<style scoped>
.footer-container {
  position: fixed;
  bottom: 0;
  display: flex;
  justify-content: space-around;
  width: 100%;
  height: 7vh;
  background-color: var(--light-onyx);
  color: var(--aquamarine);
  text-align:center;
  margin-top: 2vh;
}
h1{
  font-size: 4vh;
}

</style>
