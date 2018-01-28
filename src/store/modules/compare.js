import {setStats} from '../../utils/eq'

export default {
  state: {
    canAddToEq: true,
    compareItems: [],
    comparePairs: []
  },
  getters: {
    canAddToEq: state => state.canAddToEq,
    compareItems: state => state.compareItems,
    comparePairs: state => state.comparePairs
  },
  mutations: {
    toggleCanAddToEq: state => {
      state.canAddToEq = !state.canAddToEq
    },
    addCompareItem: (state, item) => {
      state.compareItems.push(item)
    },
    removeCompareItem: (state, item) => {
      state.compareItems = state.compareItems.filter(el => el.pk !== item.pk)
    },
    clearCompareItems: state => {
      state.compareItems = []
    },
    addPair: (state, pair) => {
      state.comparePairs.unshift(pair)
    },
    clearCompareParis: state => {
      state.comparePairs = []
    }
  },
  actions: {
    /**
     * Adds item to comparedItems and compares it with other items
     */
    compareItem ({ commit, state, dispatch }, payload) {
      for (let item of state.compareItems) {
        if (payload.item.pk === item.pk) {
          payload.callback && payload.callback('Już porównywany')
          return
        }
      }
      dispatch('createPairForItem', payload.item)
      commit('addCompareItem', payload.item)
      payload.callback && payload.callback('Porównuję')
    },
    /**
     * Compares an item with other items of the same type
     */
    createPairForItem ({ commit, state }, item) {
      let pair = {
        item: item,
        itemStats: setStats({
          unknownPlacement: item
        }),
        comparisons: []
      }
      const otherItemsOfTheSameType = state.compareItems.filter(
        comparedItem => comparedItem.type === item.type && comparedItem.pk !== item.pk
      )
      for (let comparedItem of otherItemsOfTheSameType) {
        pair.comparisons.push({
          'item': comparedItem,
          'itemStats': setStats({
            unknownPlacement: comparedItem
          })
        })
      }
      commit('addPair', pair)
    },
    /**
     * Creates pairs for all compared items.
     */
    initPairs ({ state, dispatch }) {
      for (let item of state.compareItems) {
        dispatch('createPairForItem', item)
      }
    },
    uncompareItem ({ commit, state }, payload) {
      commit('removeCompareItem', payload.item)
      payload.callback('Usunięto z porównania')
    },
    removeAllItems ({ commit }) {
      commit('clearCompareItems')
      commit('clearCompareParis')
    }
  }
}