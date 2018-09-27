<template>
    <div class="note-form">
      <form class="create-note" v-on:submit.prevent="createNote()">
          <textarea name="content" id="note-content" placeholder="Nova nota..." v-model="content"></textarea>
          <button type="submit">+</button>
      </form>
    </div>
</template>
<script>
export default {
  data () {
    return {
      content: '',
      errors: []
    }
  },
  methods: {
    createNote () {
      if (this.content.trim()) {
        this.$emit('create-note', this.content)
        this.content = ''
      }
    }
  }
}
</script>
<style>
.note-form {
    flex-basis: 100%;
}
form.create-note {
    position: relative;
    width: 480px;
    margin: 35px auto 100px auto;
    background: #fff;
    padding: 15px;
    border-radius: 2px;
    box-shadow: 0 1px 5px #ccc;
}
form.create-note textarea{
    resize: none;
    width: 100%;
    border: none;
    padding: 4px;
    outline: none;
    font-size: 1.2em;
  }
form.create-note button{
    position: absolute;
    right: 10px;
    bottom: -18px;
    background: #41b883;
    color: #fff;
    border: none;
    border-radius: 50%;
    width: 36px;
    height: 36px;
    box-shadow: 0 1px 3px rgba(0,0,0,0.3);
    cursor: pointer;
    outline: none;
  }
</style>
