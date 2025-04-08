<template>

    <view class="w-full max-w-md ">
      <view class="text-center">
        <!-- 用户信息卡片 -->
        <view class="bg-white p-6 rounded-xl shadow-lg my-4 transform scale-100">
          <view class="flex items-center">
            <image
              class="w-24 h-24 rounded-full mr-4 border-4 border-blue-500"
              :src="user.avatar"
              alt="用户头像"
            ></image>
            <view class="text-xl font-bold text-gray-800">{{ user.name }}</view>
          </view>
        </view>

        <!-- 登录按钮 -->
        <wd-button
          v-if="!user.isLogged"
          @click="showLoginModal = true"
          class="my-2 w-full bg-blue-500 hover:bg-blue-600 text-white font-bold py-3 rounded-xl transition-all duration-300"
        >
          登录
        </wd-button>

        <!-- 注册按钮 -->
        <wd-button
          v-if="!user.isLogged"
          @click="showRegisterModal = true"
          class="my-2 w-full bg-green-500 hover:bg-green-600 text-white font-bold py-3 rounded-xl transition-all duration-300"
        >
          注册
        </wd-button>

        <!-- 登出按钮 -->
        <wd-button
          v-else
          type="error"
          @click="logout"
          class="my-2 w-full bg-red-500 hover:bg-red-600 text-white font-bold py-3 rounded-xl transition-all duration-300"
        >
          登出
        </wd-button>
      </view>
    </view>

    <!-- 登录弹出层 -->
    <view v-if="showLoginModal" class="fixed inset-0 bg-black bg-opacity-50 flex items-center justify-center z-35 ">
      <view class="bg-white p-8 rounded-xl shadow-xl w-96 transform scale-100">
        <view class="text-xl font-bold mb-6 text-center text-gray-800">登录</view>
        <view class="mb-6">
          <text class="block text-base mb-2 text-gray-600">账号：</text>
          <input class="border border-gray-300 p-3 rounded-lg w-full focus:outline-none focus:border-blue-500 transition-all duration-300" v-model="account" placeholder="请输入账号" />
        </view>
        <view class="mb-6">
          <text class="block text-base mb-2 text-gray-600">密码：</text>
          <input class="border border-gray-300 p-3 rounded-lg w-full focus:outline-none focus:border-blue-500 transition-all duration-300" v-model="password" type="password" placeholder="请输入密码" />
        </view>
        <view class="flex justify-between">
          <wd-button @click="showLoginModal = false" class="bg-gray-300 hover:bg-gray-400 text-gray-800 font-bold py-3 px-6 rounded-lg transition-all duration-300">
            取消
          </wd-button>
          <wd-button type="primary" @click="handleLogin" class="bg-blue-500 hover:bg-blue-600 text-white font-bold py-3 px-6 rounded-lg transition-all duration-300">
            登录
          </wd-button>
        </view>
      </view>
    </view>

    <!-- 注册弹出层 -->
    <view v-if="showRegisterModal" class="fixed inset-0 bg-black bg-opacity-50 flex items-center justify-center z-35 ">
      <view class="bg-white p-8 rounded-xl shadow-xl w-96 transform scale-100">
        <view class="text-xl font-bold mb-6 text-center text-gray-800">注册</view>
        <view class="mb-6">
          <text class="block text-base mb-2 text-gray-600">账号：</text>
          <input class="border border-gray-300 p-3 rounded-lg w-full focus:outline-none focus:border-blue-500 transition-all duration-300" v-model="registerAccount" placeholder="请输入账号" />
        </view>
        <view class="mb-6">
          <text class="block text-base mb-2 text-gray-600">密码：</text>
          <input class="border border-gray-300 p-3 rounded-lg w-full focus:outline-none focus:border-blue-500 transition-all duration-300" v-model="registerPassword" type="password" placeholder="请输入密码" />
        </view>
        <view class="flex justify-between">
          <wd-button @click="showRegisterModal = false" class="bg-gray-300 hover:bg-gray-400 text-gray-800 font-bold py-3 px-6 rounded-lg transition-all duration-300">
            取消
          </wd-button>
          <wd-button type="primary" @click="handleRegister" class="bg-green-500 hover:bg-green-600 text-white font-bold py-3 px-6 rounded-lg transition-all duration-300">
            注册
          </wd-button>
        </view>
      </view>
    </view>
  <!-- </view> -->
</template>

<script lang="ts" setup>
import { ref } from 'vue'

const storedUser = uni.getStorageSync('userInfo')
const user = ref(
  storedUser && storedUser.isLogged !== undefined
    ? storedUser
    : { isLogged: false, name: '', avatar: '' }
)

if (!storedUser || storedUser.isLogged === undefined) {
  uni.setStorageSync('userInfo', user.value)
}

// 登录弹出层显示状态
const showLoginModal = ref(false)

// 注册弹出层显示状态
const showRegisterModal = ref(false)

// 账号和密码绑定
const account = ref('')
const password = ref('')
const registerAccount = ref('')
const registerPassword = ref('')

// 登录逻辑
const handleLogin = async () => {
  const loginUrl = 'http://localhost:8000/api/login'
  try {
    const response = await uni.request({
      url: loginUrl,
      method: 'POST',
      data: {
        account: account.value,
        password: password.value
      }
    })
    if (response.statusCode === 200 && response.data.success) {
      const userData = response.data.data
      // user.value.isLogged = true
      // user.value.name = userData.name
      // user.value.avatar = userData.avatar
      uni.setStorageSync('userInfo', {
        isLogged: true,
        name: userData.name,
        avatar: userData.avatar
      })

      uni.showToast({
        title: '登录成功',
        icon: 'success'
      })
      showLoginModal.value = false
    } else {
      uni.showToast({
        title: response.data.msg || '登录失败',
        icon: 'none'
      })
    }
  } catch (error) {
    console.error('请求失败:', error)
    uni.showToast({
      title: '请求失败，请检查网络',
      icon: 'none'
    })
  }
  //刷新当前页面
  uni.reLaunch({
    url: '/pages/about/about'
  })
}

// 注册逻辑
const handleRegister = async () => {
  const registerUrl = 'http://localhost:8000/api/register'
  try {
    const response = await uni.request({
      url: registerUrl,
      method: 'POST',
      data: {
        account: registerAccount.value,
        password: registerPassword.value
      }
    })
    if (response.statusCode === 200 && response.data.success) {
      uni.showToast({
        title: '注册成功',
        icon: 'success'
      })
      showRegisterModal.value = false
    } else {
      uni.showToast({
        title: response.data.msg || '注册失败',
        icon: 'none'
      })
    }
  } catch (error) {
    console.error('请求失败:', error)
    uni.showToast({
      title: '请求失败，请检查网络',
      icon: 'none'
    })
  }
}

// 登出逻辑
const logout = () => {
  user.value.isLogged = false
  user.value.name = ''
  user.value.avatar = ''
  uni.showToast({
    title: '已登出',
    icon: 'none'
  })
  uni.removeStorageSync('userInfo')
  uni.reLaunch({
    url: '/pages/about/about'
  })
  // 清除登录状态
  uni.setStorageSync('userInfo', {
    isLogged: false,
    name: '',
    avatar: ''
  })
  // 关闭登录弹出层
}
</script>