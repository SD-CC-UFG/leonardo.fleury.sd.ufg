<template>
  <div id="app" class="container">
    <create-note-form></create-note-form>
    <notes></notes>
  </div>
</template>
<script>
import Notes from './components/notes/Index'
import CreateNoteForm from './components/notes/Create'

export default {
  name: 'App',
  components: {
    Notes,
    CreateNoteForm
  }
}
</script>
<style>
.container {
  width: 960px;
  margin: auto;
}
</style>
