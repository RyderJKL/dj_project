import Vue from 'vue'
import Router from 'vue-router'
import { constRoutes, asyncRoutes } from './routes'
Vue.use(Router)

export default new Router({
  routes: [...constRoutes, ...asyncRoutes]
})
