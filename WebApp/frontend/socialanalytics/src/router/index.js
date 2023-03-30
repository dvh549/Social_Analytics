import { createRouter, createWebHistory } from 'vue-router'
import Home from '../views/Home.vue'
import LiveAnalysis from '../views/LiveAnalysis.vue'


const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home
  },
  {
    path: '/liveanalysis',
    name: 'LiveAnalysis',
    component: LiveAnalysis
  }
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
