<template>
    <div class="note child">
        <p class="content">{{note.content}}</p>
    </div>
</template>
<script>
export default {
  props: ['note']
}
</script>
<style>
.content {
    padding: 0 15px;
}
.note {
    margin: 5px;
    padding: 5px;
    width: 200px;
    min-height: 200px;
    background-color: antiquewhite;
    box-shadow: 0px 2px 2px rgb(0, 0, 0, 0.25);
}
</style>
