<script setup lang="ts">
  import {RouterLink} from "vue-router"

</script>


<template>
  <div class="header-container">
    <RouterLink to="/">
      <h1>Wrkt</h1>
    </RouterLink>
  </div>
</template>

<style scoped>
.header-container {
  position: fixed;
  top: 0;
  left: 0;
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
