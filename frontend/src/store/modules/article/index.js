import * as aTypes from '../../actionTypes/article'
import * as mTypes from '../../mutationTypes/article'

import api from 'api'

const state = {

}

const getters = {

}

const actions = {
  async [aTypes.GET_ALL_ARTICLES] () {
    try {
      const articles = api.article[aTypes.GET_ALL_ARTICLES]
      console.log(articles)
    } catch (e) {
    }
  }
}

const mutations = {
  [mTypes.SET_ALL_ARTICLES] (state) {

  }
}

export default {
  namespaced: true,
  state,
  getters,
  mutations,
  actions
}
