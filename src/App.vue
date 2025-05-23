<script setup>
import AppHeader from "./components/AppHeader.vue";
import AppFooter from "./components/AppFooter.vue";
import DashboardPage from "./pages/DashboardPage.vue";
import WorkoutPage from "./pages/WorkoutPage.vue";
import { ref } from "vue";

const pages = { Dashboard: DashboardPage, Workout: WorkoutPage };
const currentPage = ref("Dashboard");

function updatePage(page) {
  currentPage.value = page;
}
</script>

<template>
  <header>
    <AppHeader text="Welcome {User}!" />
  </header>

  <main>
    <component :is="pages[currentPage]" @update-page="updatePage" />
  </main>

  <footer>
    <AppFooter />
  </footer>
</template>

<style scoped>
header {
  display: block;
  border-bottom: white 2px solid;
}

main {
  display: block;
}

footer {
  width: 100%;
}
</style>
