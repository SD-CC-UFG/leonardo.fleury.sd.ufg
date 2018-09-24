<template>
  <div class="notes parent">
    <note v-for="note in notes" :note="note" :key="note.id">
    </note>
  </div>
</template>
<script>
import Note from './Note'

export default {
  components: {
    Note
  },
  data () {
    return {
      notes: [],
      errors: []
    }
  },
  created () {
    this.axios.get('http://127.0.0.1:5000/')
      .then(response => {
        this.notes = response.data
      })
      .catch(e => {
        this.errors.push(e)
        console.error(e)
      })
  }
}
</script>
<style>
.parent {
  display: flex;
  flex-direction: row;
  flex-wrap: wrap;
  justify-content: space-around;
}
</style>
