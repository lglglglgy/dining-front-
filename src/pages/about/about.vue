<route lang="json5">
{
  style: {
    navigationBarTitleText: '我的',
  },
}
</route>

<template>
  <view
    class="bg-white overflow-hidden pt-2 px-4"
    :style="{ marginTop: safeAreaInsets?.top + 'px' }"
  >
  <view class="flex flex-col h-screen justify-start items-center bg-gradient-to-b from-blue-100 to-white p-6">
    <login />
    <!-- <UploadComp /> -->
    <info />
  </view>
  </view>
</template>

<script lang="ts" setup>
import { ref } from 'vue'
import login from './components/login.vue'


// 尝试从全局存储中读取用户信息，没有则使用默认值
const userInfo = ref(uni.getStorageSync('userInfo') || {
  isLogged: false,
  name: '请登陆后使用',
  avatar: 'https://c-ssl.dtstatic.com/uploads/item/202004/14/20200414210134_qbeyi.thumb.400_0.jpg'
})
import info from './components/info.vue'

// 获取屏幕边界到安全区域距离
const { safeAreaInsets } = uni.getSystemInfoSync()
</script>

<style lang="scss" scoped>
.test-css {
  // mt-4=>1rem=>16px;
  margin-top: 16px;
}
</style>
