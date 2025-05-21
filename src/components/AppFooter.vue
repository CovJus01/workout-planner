<script setup></script>

<template>
  <div>
    <a href="#">Home</a>
    <a href="#">Add</a>
    <a href="#">Settings</a>
  </div>
</template>

<style scoped>
a {
  text-decoration: none;
  color: white;
}

div {
  display: flex;
  position: fixed;
  top: 95vh;
  left: 0;
  min-height: 5vh;
  width: 100%;
  justify-content: space-around;
  border-top-left-radius: 5px;
  border-top-right-radius: 5px;
  background-color: #2f2f2f;
}
</style>
