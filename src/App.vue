<script setup>
import AppHeader from "./components/AppHeader.vue";
import AppFooter from "./components/AppFooter.vue";
import DashboardPage from "./pages/DashboardPage.vue";
</script>

<template>
  <header>
    <AppHeader text="Welcome {User}!" />
  </header>

  <main>
    <DashboardPage />
    <WorkoutTable />
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
