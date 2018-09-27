<template>
    <div class="note">
        <div class="note-buttons">
            <button class="edit-button" disabled></button>
            <button class="delete-button" @click="remove"></button>
        </div>
        <p class="content">{{note.content}}</p>
    </div>
</template>
<script>
export default {
  props: ['note'],
  methods: {
    remove () {
      this.$emit('delete-note', this.note)
    },
    edit () {},
    save () {
      this.$emit('save-note', this.note)
    }
  }
}
</script>
<style>
.note-buttons {
  display: flex;
  justify-content: flex-end;
  height: 35px;
  background-color: rgb(245, 230, 210);
}

.note-buttons button {
  height: 25px;
  width: 25px;
  margin: 5px;
  padding: 0;
  background-color: rgba(0, 0, 0, 0);
  border: none;
  background-size: 100%;
  background-repeat: no-repeat;
  background-position: 50% 50%;
}

.edit-button {
  background-image: url(/static/icons/software_pencil.svg);
}

.delete-button {
  background-image: url(/static/icons/basic_trashcan.svg);
}

.content {
  padding: 0 15px;
}

.note {
  margin: 5px;
  width: 200px;
  min-height: 200px;
  background-color: antiquewhite;
  box-shadow: 0px 2px 2px rgb(0, 0, 0, 0.25);
}
</style>
