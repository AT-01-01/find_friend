<template>
  <el-container class="layout">
    <el-aside width="200px" class="sider">
      <div class="brand">搭子前端</div>
      <el-menu :default-active="$route.path" router>
        <el-menu-item index="/users">用户</el-menu-item>
        <el-menu-item index="/match">匹配</el-menu-item>
        <el-menu-item index="/activities">活动</el-menu-item>
        <el-menu-item index="/chats">聊天</el-menu-item>
      </el-menu>
    </el-aside>
    <el-main class="main">
      <router-view />
    </el-main>
  </el-container>
</template>

<style scoped>
.layout {
  min-height: 100vh;
}

.sider {
  border-right: 1px solid #eceef2;
  background: #fff;
}

.brand {
  padding: 16px;
  font-size: 18px;
  font-weight: 600;
}

.main {
  background: #f6f8fa;
}
</style>
