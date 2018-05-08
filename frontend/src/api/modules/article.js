import http from '../core/http'
import apiConfig from '../core/config'

import * as aTypes from 'store/actionTypes/article'

export default {
  [aTypes.GET_ALL_ARTICLES] () {
    const uri = `${apiConfig.prefix}/articles`
    return http.get(uri)
  }
  // getArticleWidthId (id) {
  //   const uri = `${apiConfig.prefix}/article${id}`
  //   return http.get(uri)
  // }
}
