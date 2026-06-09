import { createRouter, createWebHistory } from 'vue-router'
import Dashboard from '@/pages/Dashboard.vue'
import DevComponents from '@/pages/DevComponents.vue'

const routes = [
  { path: "/", component: Dashboard },

]

// Add route to display components only when development is active
if (process.env.NODE_ENV === 'development') {
  routes.push({ path: "/dev/components", component: DevComponents })
}

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes,
})

export default router
