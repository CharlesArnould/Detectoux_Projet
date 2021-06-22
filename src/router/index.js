import { createRouter, createWebHistory } from 'vue-router'
import Home from '../views/Home.vue'
import Contribue0 from '../views/Contribue0.vue'
import Contribue3 from '../views/Contribue3.vue'
import Test3_1 from '../views/Test3_1.vue'
import Test3_2 from '../views/Test3_2.vue'

const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home
  },
  {
    path: '/',
    name: 'Contribue0',
    component: Contribue0
  },
  {
    path: '/',
    name: 'Contribue3',
    component: Contribue3
  },
  {
    path: '/',
    name: 'Test3_1',
    component: Test3_1

  },
  {
    path: '/',
    name: 'Test3_2',
    component: Test3_2
  },
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
