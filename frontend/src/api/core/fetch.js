import axios from 'axios'
import humps from 'humps'
import { Message } from 'element-ui'

const fetch = axios.create({
  timeout: 30000
})

fetch.interceptors.response.use(
  response => {
    const res = response.data
    if (res.status !== 'success') {
      if (res.error && res.error.level < 2) {
        Message({
          message: response.data.error.message,
          type: 'error',
          duration: 3 * 1000
        })
      }

      if (res.error && res.error.level === 2) {
        Message({
          message: '出错啦～！',
          type: 'error',
          duration: 3 * 1000
        })
      }

      if (res.error && res.error.code === 10001) {
        window.location.assign('/auth/login')
      }

      return Promise.reject(res.error.message)
    }

    return Promise.resolve(humps.camelizeKeys(res.data))
  },
  error => {
    Message({
      message: error.message,
      type: 'error',
      duration: 5 * 1000
    })
    return Promise.reject(error)
  })

export default fetch
