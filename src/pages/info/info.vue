<route lang="json5">
{
  style: {
    navigationBarTitleText: '食堂人流量情况',
    navigationStyle: 'custom'
  }
}
</route>

<template>
  <div>
    <div class="chart-container" style="position: relative;">
      <div class="bar-chart" ref="barChart" style="height: 400px;"></div>
    </div>
    <!-- 新增的建议矩形框 -->
    <div class="suggestion-container">
      <div class="suggestion-title">选择建议</div>
      <div class="suggestion-content" v-html="suggestionText"></div>
    </div>
  </div>
</template>

<script>
import { ref, onMounted } from 'vue'
import axios from 'axios'
import * as echarts from 'echarts'

export default {
  name: 'Info',
  setup() {
    const barChart = ref(null)
    const suggestionText = ref('加载中...')
    let chartInstance = null

    const fetchData = async () => {
      try {
        const response = await axios.get('http://localhost:3000/da')
        return response.data
      } catch (error) {
        console.error('数据获取失败：', error)
        return []
      }
    }

    const getColorByPercentage = (percentage) => {
      const hue = 120 - (percentage * 1.2)
      return `hsl(${hue}, 100%, 50%)`
    }

    const initChart = async () => {
      const data = await fetchData()
      const categories = data.map(item => item.category)
      const values = data.map(item => item.value)
      const colors = values.map(value => getColorByPercentage(value))

      const options = {
        title: {
          text: '食堂人流量情况',
          left: 'center',
          top: '20px'
        },
        tooltip: {
          formatter: '{a} <br/>{b}: {c}%'
        },
        xAxis: {
          type: 'category',
          data: categories
        },
        yAxis: {
          type: 'value',
          max: 120,
          axisLabel: {
            formatter: '{value}%'
          },
          interval: 20
        },
        series: [{
          name: '数值',
          type: 'bar',
          data: values.map((value, index) => ({
            value: value,
            itemStyle: {
              color: colors[index]
            }
          }))
        }]
      }
      chartInstance = echarts.init(barChart.value)
      chartInstance.setOption(options)

      // 根据数据计算建议
      if (values.length) {
        //如果所有数据均大于80，则给出建议不要就餐
        if (values.every(value => value > 80)) {
          suggestionText.value = '建议您选择其他就餐时间。'
        } else if (values.some(value => value > 80)) {
          //找的最小的
          const minValue = Math.min(...values)
          const minIndex = values.indexOf(minValue)
          suggestionText.value = `人流量较大，建议您前往 <span style="color: red; font-weight: bold;">${categories[minIndex]}</span> 就餐。`;
        } else {
          suggestionText.value = '人流量适中，欢迎选择任一食堂就餐！'
        }
      } else {
        suggestionText.value = '暂无数据建议。'
      }
    }

    onMounted(() => {
      initChart()
      window.addEventListener('resize', () => {
        if (chartInstance) {
          chartInstance.resize()
        }
      })
    })

    return {
      barChart,
      suggestionText
    }
  }
}
</script>

<style scoped>
.chart-container {
  background-color: #fff;
  border: 1px solid #ddd;
  border-radius: 12px;
  padding: 16px;
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
  overflow: hidden;
  margin-bottom: 16px;
}

.bar-chart {
  width: 100%;
  height: 400px;
}

.suggestion-container {
  background-color: #fff;
  border: 1px solid #ddd;
  border-radius: 12px;
  padding: 16px;
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
}

.suggestion-title {
  font-size: 18px;
  font-weight: bold;
  margin-bottom: 8px;
}

.suggestion-content {
  font-size: 16px;
}
.highlight {
  color: red !important; /* 使用 !important 确保样式不会被覆盖 */
  font-weight: bold;
}
.suggestion-content {
  font-size: 16px;
  line-height: 1.5; /* 新增行高以改善可读性 */
}
</style>