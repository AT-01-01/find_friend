<script setup lang="ts">
import { onMounted, reactive, ref } from 'vue'
import { ElMessage } from 'element-plus'
import apiClient from '../api/client'

type Activity = {
  id: number
  author_id: number
  title: string
  content: string
  city: string | null
}

const form = reactive({
  author_id: 1,
  title: '',
  content: '',
  city: '',
})

const activities = ref<Activity[]>([])

const loadActivities = async () => {
  const { data } = await apiClient.get<Activity[]>('/activities/')
  activities.value = data
}

const createActivity = async () => {
  await apiClient.post('/activities/', {
    ...form,
    city: form.city || null,
  })
  ElMessage.success('活动发布成功')
  await loadActivities()
}

onMounted(loadActivities)
</script>

<template>
  <h2>活动模块</h2>
  <el-row :gutter="16">
    <el-col :span="10">
      <el-card header="发布活动">
        <el-form label-width="90px">
          <el-form-item label="作者ID"><el-input-number v-model="form.author_id" :min="1" /></el-form-item>
          <el-form-item label="标题"><el-input v-model="form.title" /></el-form-item>
          <el-form-item label="内容"><el-input v-model="form.content" type="textarea" /></el-form-item>
          <el-form-item label="城市"><el-input v-model="form.city" /></el-form-item>
        </el-form>
        <el-button type="primary" @click="createActivity">发布</el-button>
      </el-card>
    </el-col>
    <el-col :span="14">
      <el-card header="活动列表">
        <el-button size="small" @click="loadActivities">刷新</el-button>
        <el-table :data="activities" style="margin-top: 12px" empty-text="暂无活动">
          <el-table-column prop="id" label="ID" width="70" />
          <el-table-column prop="author_id" label="作者ID" width="90" />
          <el-table-column prop="title" label="标题" />
          <el-table-column prop="content" label="内容" />
          <el-table-column prop="city" label="城市" width="100" />
        </el-table>
      </el-card>
    </el-col>
  </el-row>
</template>
