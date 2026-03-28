import { createRouter, createWebHistory } from 'vue-router'
import ActivityView from '../views/ActivityView.vue'
import ChatView from '../views/ChatView.vue'
import MatchView from '../views/MatchView.vue'
import UserView from '../views/UserView.vue'

const router = createRouter({
  history: createWebHistory(),
  routes: [
    { path: '/', redirect: '/users' },
    { path: '/users', component: UserView, meta: { title: '用户' } },
    { path: '/match', component: MatchView, meta: { title: '匹配' } },
    { path: '/activities', component: ActivityView, meta: { title: '活动' } },
    { path: '/chats', component: ChatView, meta: { title: '聊天' } },
  ],
})

export default router
