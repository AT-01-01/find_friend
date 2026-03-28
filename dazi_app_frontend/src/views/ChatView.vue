<script setup lang="ts">
import { reactive, ref } from 'vue'
import { ElMessage } from 'element-plus'
import apiClient from '../api/client'

type ChatSession = {
  id: number
  user_a_id: number
  user_b_id: number
}

const createForm = reactive({
  user_a_id: 1,
  user_b_id: 2,
})

const queryUserId = ref(1)
const sessions = ref<ChatSession[]>([])

const createSession = async () => {
  await apiClient.post('/chats/sessions', createForm)
  ElMessage.success('会话创建成功')
}

const listSessions = async () => {
  const { data } = await apiClient.get<ChatSession[]>(`/chats/sessions/${queryUserId.value}`)
  sessions.value = data
}
</script>

<template>
  <h2>聊天模块</h2>
  <el-row :gutter="16">
    <el-col :span="10">
      <el-card header="创建聊天会话">
        <el-form label-width="110px">
          <el-form-item label="用户A ID">
            <el-input-number v-model="createForm.user_a_id" :min="1" />
          </el-form-item>
          <el-form-item label="用户B ID">
            <el-input-number v-model="createForm.user_b_id" :min="1" />
          </el-form-item>
        </el-form>
        <el-button type="primary" @click="createSession">创建会话</el-button>
      </el-card>
    </el-col>
    <el-col :span="14">
      <el-card header="查询用户会话">
        <el-form inline>
          <el-form-item label="用户ID">
            <el-input-number v-model="queryUserId" :min="1" />
          </el-form-item>
          <el-form-item>
            <el-button @click="listSessions">查询</el-button>
          </el-form-item>
        </el-form>
        <el-table :data="sessions" style="margin-top: 12px" empty-text="暂无会话">
          <el-table-column prop="id" label="会话ID" width="90" />
          <el-table-column prop="user_a_id" label="用户A" />
          <el-table-column prop="user_b_id" label="用户B" />
        </el-table>
      </el-card>
    </el-col>
  </el-row>
</template>
