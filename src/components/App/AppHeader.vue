<script setup lang="ts">
  import {RouterLink} from "vue-router"

</script>


<template>
  <div class="header-container">
    <RouterLink to="/">
      <h1 class ="oswald-bold">Wrkt</h1>
    </RouterLink>
  </div>
</template>

<style scoped>
.header-container {
  width: 100%;
  height: 7vh;
  background-color: var(--dark-onyx);
  color: var(--aquamarine);
  text-align:center;
  margin-bottom: 2vh;
}
h1{
  padding-top:1vh;
}

</style>
