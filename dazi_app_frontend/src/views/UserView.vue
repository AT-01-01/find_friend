<script setup lang="ts">
import { reactive, ref } from 'vue'
import { ElMessage } from 'element-plus'
import apiClient from '../api/client'

type UserRead = {
  id: number
  username: string
  email: string
  city: string | null
  interests: string | null
  bio: string | null
}

const registerForm = reactive({
  username: '',
  email: '',
  password: '',
  city: '',
  interests: '',
  bio: '',
})

const loginForm = reactive({
  username: '',
  password: '',
})

const currentUser = ref<UserRead | null>(null)
const token = ref('')

const registerUser = async () => {
  const { data } = await apiClient.post<UserRead>('/users/register', registerForm)
  currentUser.value = data
  ElMessage.success(`注册成功，用户ID：${data.id}`)
}

const loginUser = async () => {
  const { data } = await apiClient.post<{ access_token: string; token_type: string }>(
    '/users/login',
    loginForm,
  )
  token.value = `${data.token_type} ${data.access_token}`
  ElMessage.success('登录成功')
}
</script>

<template>
  <h2>用户模块</h2>
  <el-row :gutter="16">
    <el-col :span="12">
      <el-card header="注册">
        <el-form label-width="90px">
          <el-form-item label="用户名"><el-input v-model="registerForm.username" /></el-form-item>
          <el-form-item label="邮箱"><el-input v-model="registerForm.email" /></el-form-item>
          <el-form-item label="密码"><el-input v-model="registerForm.password" type="password" /></el-form-item>
          <el-form-item label="城市"><el-input v-model="registerForm.city" /></el-form-item>
          <el-form-item label="兴趣"><el-input v-model="registerForm.interests" /></el-form-item>
          <el-form-item label="简介"><el-input v-model="registerForm.bio" type="textarea" /></el-form-item>
        </el-form>
        <el-button type="primary" @click="registerUser">提交注册</el-button>
      </el-card>
    </el-col>
    <el-col :span="12">
      <el-card header="登录">
        <el-form label-width="90px">
          <el-form-item label="用户名"><el-input v-model="loginForm.username" /></el-form-item>
          <el-form-item label="密码"><el-input v-model="loginForm.password" type="password" /></el-form-item>
        </el-form>
        <el-button type="success" @click="loginUser">登录</el-button>
        <el-alert v-if="token" style="margin-top: 12px" type="success" :closable="false">
          <template #title>Token：{{ token }}</template>
        </el-alert>
      </el-card>
      <el-card v-if="currentUser" header="最近注册用户" style="margin-top: 16px">
        <el-descriptions :column="1" border>
          <el-descriptions-item label="ID">{{ currentUser.id }}</el-descriptions-item>
          <el-descriptions-item label="用户名">{{ currentUser.username }}</el-descriptions-item>
          <el-descriptions-item label="邮箱">{{ currentUser.email }}</el-descriptions-item>
          <el-descriptions-item label="城市">{{ currentUser.city }}</el-descriptions-item>
          <el-descriptions-item label="兴趣">{{ currentUser.interests }}</el-descriptions-item>
          <el-descriptions-item label="简介">{{ currentUser.bio }}</el-descriptions-item>
        </el-descriptions>
      </el-card>
    </el-col>
  </el-row>
</template>
