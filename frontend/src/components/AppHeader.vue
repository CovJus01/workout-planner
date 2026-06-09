<script setup lang='ts'>
import { useRouter } from 'vue-router'

const router = useRouter()

const navigateToHome = () => {
  router.push("/")
}

</script>

<template>
  <div class="header-container">
    <div class="app-title" @click="navigateToHome">
      Commonect
    </div>
  </div>
</template>

<style scoped>
.header-container {
  background-color: #1A1A1A;
  display: flex;
  align-items: center;
  justify-content: space-around;
  height: 8vh;
  width: 100%;
}

.app-title {
  color: #EAEAEA;
  font-size: 3rem;
}
</style>
