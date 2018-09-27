<template>
  <div id="app" class="container">
    <notes></notes>
  </div>
</template>
<script>
import Notes from './components/notes/Index'

export default {
  name: 'App',
  components: {
    Notes
  }
}
</script>
<style>
body {
  font-family: 'Lucida Sans', 'Lucida Sans Regular', 'Lucida Grande', 'Lucida Sans Unicode', Geneva, Verdana, sans-serif;
  background-color: rgb(250, 250, 250);
}
.container {
  width: 960px;
  margin: auto;
  height: 100vh;
}
</style>
