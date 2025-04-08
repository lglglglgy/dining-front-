// backend.js
const express = require('express')
const cors = require('cors')

const app = express()
const port = 3000

// 允许跨域请求（如需要）
app.use(cors())

app.get('/da', (req, res) => {
  // 返回模拟数据
  res.json([
    { category: '食堂1', value: 10 },
    { category: '食堂2', value: 70 },
    { category: '食堂3', value: 110 }
  ])
})

app.listen(port, () => {
  console.log(`服务器已启动，监听 http://localhost:${port}`)
})
