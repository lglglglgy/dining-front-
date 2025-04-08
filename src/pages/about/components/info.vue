<template>
  <view v-if="user.isLogged" class="flex justify-around items-center p-4">
    <!-- 历史订单按钮 -->
    <view class="button-container" @click="goToHistoryOrders">
      <image class="icon" src="/static/icons/history-orders.png" />
      <text class="label">历史订单</text>
    </view>
    <!-- 进行中订单按钮 -->
    <view class="button-container" @click="goToOngoingOrders">
      <image class="icon" src="/static/icons/ongoing-orders.png" />
      <text class="label">进行中订单</text>
    </view>
    <!-- 余额按钮 -->
    <view class="button-container" @click="goToBalance">
      <image class="icon" src="/static/icons/balance.png" />
      <text class="label">余额</text>
    </view>
    <!-- 开发中按钮 -->
    <view class="button-container" @click="showUnderDevelopment">
      <image class="icon" src="/static/icons/under-development.png" />
      <text class="label">开发中</text>
    </view>
  </view>
  <!-- 显示生成的二维码 -->
  <view v-if="qrCodeUrl" class="qrcode-container">
    <image :src="qrCodeUrl" alt="二维码"  />
  </view>
</template>

<script lang="ts" setup>
import { ref } from 'vue'
import QRCode from 'qrcode'

// 从全局存储中获取用户信息
const storedUser = uni.getStorageSync('userInfo')
const user = ref(
  storedUser && storedUser.isLogged !== undefined
    ? storedUser
    : { isLogged: false, name: '', avatar: '' }
)


// 定义保存二维码图片数据的响应式变量
const qrCodeUrl = ref('')

// 获取userid并拼接时间生成二维码数据
const uid = storedUser.name
  ? storedUser.name
  : 'guest' // 默认值为 'guest'
const qrData = uid + "date"+ new Date().toISOString()

QRCode.toDataURL(qrData, (err, url) => {
  if (err) throw err;
  qrCodeUrl.value = url
});

// 历史订单按钮点击事件
const goToHistoryOrders = () => {
  uni.navigateTo({
    url: "/pages/about/components/history-orders",
  });
};

// 进行中订单按钮点击事件
const goToOngoingOrders = () => {
  uni.navigateTo({
    url: '/pages/ongoing-orders/ongoing-orders',
  });
};

// 余额按钮点击事件
const goToBalance = () => {
  uni.navigateTo({
    url: '/pages/balance/balance',
  });
};

// 开发中按钮点击事件
const showUnderDevelopment = () => {
  // Placeholder for under-development functionality
};
</script>

<style lang="scss" scoped>
.button-container {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  width: 80px;
  height: 100px;
  background-color: #f5f5f5;
  border-radius: 12px;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
  cursor: pointer;
}

.icon {
  width: 40px;
  height: 40px;
  margin-bottom: 8px;
}

.label {
  font-size: 14px;
  color: #333;
}

.qrcode-container {
  display: flex;
  justify-content: center;
  margin-top: 20px;
}
</style>