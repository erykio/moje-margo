export const toast = {
  methods: {
    // toast (message) {
    //   this.$toast.open(message)
    // },
    success (message) {
      this.$toast.open({
        message: message,
        type: 'is-dark',
        position: 'is-bottom-right',
        queue: false,
        duration: 750
      })
    }
    // danger (message) {
    //   this.$toast.open({
    //     duration: 5000,
    //     message: message,
    //     position: 'is-bottom',
    //     type: 'is-danger'
    //   })
    // }
  }
}
