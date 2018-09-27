<template>
  <div class="notes parent">
    <create-note-form v-on:create-note="createNote">
    </create-note-form>
    <note v-for="note in notes"
      :note="note"
      :key="note.id"
      v-on:delete-note="removeNote"
      v-on:update-note="updateNote">
    </note>
  </div>
</template>
<script>
import Note from './Note'
import CreateNoteForm from './Create'

export default {
  components: {
    Note,
    CreateNoteForm
  },
  data () {
    return {
      notes: [],
      errors: []
    }
  },
  created () {
    this.getAllNotes()
  },
  methods: {
    getAllNotes () {
      this.axios
        .get('http://127.0.0.1:5000/')
        .then(response => {
          this.notes = response.data
        })
        .catch(e => {
          this.errors.push(e)
          console.error(e)
        })
    },
    removeNote (note) {
      console.log('Apagar nota ' + note.id)
      this.axios
        .delete('http://127.0.0.1:5000/' + note.id)
        .then(response => {})
        .catch(e => {
          this.errors.push(e)
          console.error(e)
        })
      this.notes.splice(note, 1)
    },
    updateNote (note) {
      this.axios
        .put('http://127.0.0.1:5000/' + note.id, {
          content: note.content
        })
        .then(response => {})
        .catch(e => {
          this.errors.push(e)
          console.error(e)
        })
    },
    createNote (note) {
      this.axios
        .post('http://127.0.0.1:5000/', {
          content: note
        })
        .then(response => {})
        .catch(e => {
          this.errors.push(e)
          console.error(e)
        })
      this.getAllNotes()
    }
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
