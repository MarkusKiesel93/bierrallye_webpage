<template>
  <DeregisterForm />
</template>

<script>
import { mapMutations } from 'vuex'

import DeregisterForm from '@/components/DeregisterForm'

export default {
  name: 'DeregisterView',
  components: {
    DeregisterForm,
  },
  methods: {
    ...mapMutations({
      setDeregisterEmail: 'setDeregisterEmail',
      setDeregisterHash: 'setDeregisterHash',
    }),
  },
  created: function() {
    if (this.$route.params.email) {
      this.setDeregisterEmail(this.$route.params.email)
    }
    if (this.$route.params.hash) {
      this.setDeregisterHash(this.$route.params.hash)
    }
  },
}
</script>
