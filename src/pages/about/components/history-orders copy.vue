<route lang="json5">
    {
      style: {
        navigationBarTitleText: '历史订单',
      },
    }

</route>

//展示历史订单
<template>
  <view class="bg-white overflow-hidden pt-2 px-4">
    <view class="flex flex-col h-screen justify-start items-center bg-gradient-to-b from-blue-100 to-white p-6">
      <view class="text-lg font-bold mb-4">历史订单</view>
      <view v-if="orders.length === 0" class="text-gray-500">暂无历史订单</view>
      <view 
        v-for="order in orders" 
        :key="order.id" 
        class="w-full border-b py-4 flex items-center cursor-pointer"
        @click="showOrderDetails(order)"
      >
        <image :src="order.image" class="w-16 h-16 rounded-lg mr-4" alt="订单图片" />
        <view class="flex-1">
          <view class="text-base font-bold">{{ order.name }}</view>
          <view class="text-sm text-gray-500">订单编号：{{ order.id }}</view>
          <view class="text-sm text-gray-500">订单时间：{{ order.date }}</view>
          <view class="text-sm text-gray-500">订单金额：￥{{ order.amount }}</view>
        </view>
      </view>
    </view>

    <!-- 详情弹窗 -->
    <view v-if="showDetails" class="fixed inset-0 bg-black bg-opacity-50 flex justify-center items-center">
      <view class="bg-white rounded-lg p-6 w-4/5 max-w-md">
        <view class="text-lg font-bold mb-4">订单详情</view>
        <view class="mb-2"><strong>名称：</strong>{{ selectedOrder.name }}</view>
        <view class="mb-2"><strong>订单编号：</strong>{{ selectedOrder.id }}</view>
        <view class="mb-2"><strong>订单时间：</strong>{{ selectedOrder.date }}</view>
        <view class="mb-2"><strong>订单金额：</strong>￥{{ selectedOrder.amount }}</view>
        <view class="mb-4"><image :src="selectedOrder.image" class="w-32 h-32 rounded-lg" alt="订单图片" /></view>
        <button @click="closeDetails" class="bg-blue-500 text-white px-4 py-2 rounded">关闭</button>
      </view>
    </view>
  </view>
</template>

<script lang="ts" setup>
import { ref } from 'vue'

// 模拟历史订单数据
const orders = ref([
  { id: 1, name: '订单1', date: '2023-10-01', amount: 100, image: 'https://via.placeholder.com/64' },
  { id: 2, name: '订单2', date: '2023-10-02', amount: 200, image: 'https://via.placeholder.com/64' },
  { id: 3, name: '订单3', date: '2023-10-03', amount: 300, image: 'https://via.placeholder.com/64' },
])

// 控制弹窗显示
const showDetails = ref(false)
const selectedOrder = ref({
  id: '',
  name: '',
  date: '',
  amount: 0,
  image: ''
})

// 显示订单详情
const showOrderDetails = (order: any) => {
  selectedOrder.value = order
  showDetails.value = true
}

// 关闭详情弹窗
const closeDetails = () => {
  showDetails.value = false
}
</script>
