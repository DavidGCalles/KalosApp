import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import dataIn from '../views/dataIn.vue'
import auth from "../components/auth.vue"
import newUser from "../components/newUser.vue"

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: HomeView
    },
    {
      path: '/about',
      name: 'about',
      // route level code-splitting
      // this generates a separate chunk (About.[hash].js) for this route
      // which is lazy-loaded when the route is visited.
      component: () => import('../views/AboutView.vue')
    },
    {
      path: "/dataIn",
      name: "dataIn",
      component: dataIn
    },
    {
      path:"/signIn",
      name: "signIn",
      component: auth
    },
    {
      path: "/signup",
      name: "signUp",
      component: newUser
    }
  ]
})

export default router
