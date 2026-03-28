<script setup lang="ts">
import { reactive, ref } from 'vue'
import apiClient from '../api/client'

type MatchUser = {
  id: number
  username: string
  city: string | null
  interests: string | null
}

const queryForm = reactive({
  city: '',
  interest_keyword: '',
})

const users = ref<MatchUser[]>([])

const searchUsers = async () => {
  const payload = {
    city: queryForm.city || null,
    interest_keyword: queryForm.interest_keyword || null,
  }
  const { data } = await apiClient.post<MatchUser[]>('/match/search', payload)
  users.value = data
}
</script>

<template>
  <h2>匹配模块</h2>
  <el-card>
    <el-form inline>
      <el-form-item label="城市">
        <el-input v-model="queryForm.city" placeholder="例如：上海" />
      </el-form-item>
      <el-form-item label="兴趣关键字">
        <el-input v-model="queryForm.interest_keyword" placeholder="例如：羽毛球" />
      </el-form-item>
      <el-form-item>
        <el-button type="primary" @click="searchUsers">搜索</el-button>
      </el-form-item>
    </el-form>
  </el-card>

  <el-card header="匹配结果" style="margin-top: 16px">
    <el-table :data="users" empty-text="暂无匹配结果">
      <el-table-column prop="id" label="ID" width="80" />
      <el-table-column prop="username" label="用户名" />
      <el-table-column prop="city" label="城市" />
      <el-table-column prop="interests" label="兴趣" />
    </el-table>
  </el-card>
</template>
