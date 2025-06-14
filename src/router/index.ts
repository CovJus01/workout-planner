import { createRouter, createWebHistory } from 'vue-router'
import DashboardView from "../views/DashboardView.vue"
import WorkoutView from "../views/WorkoutView.vue"

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {path: '/', component: DashboardView},
    {path: '/workout', component: WorkoutView}
  ],
})

export default router
