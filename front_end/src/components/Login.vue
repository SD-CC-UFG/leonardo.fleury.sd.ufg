<template>
    <form @submit.prevent="login">
        <label for="username">Usuario</label>
        <input type="text" name="username" id="username" v-model.trim="input.username" required>
        <label for="password">Senha</label>
        <input type="password" name="password" id="password" v-model.trim="input.password" required>
        <button type="submit" >Login</button>
    </form>
</template>

<script>
import {HTTP} from '../http_common'

export default {
    name: 'Login',
    data () {
        return {
            input: {
                username: "",
                password: ""
            }
        }
    },
    methods: {
        login() {
            if (this.input.username != "" && this.input.password != "") {
                HTTP.post('auth', {
                    'username': this.input.username,
                    'password': this.input.password
                })
                .then(response => {
                    console.log('user logged')
                })
                .catch(e => {
                    this.errors.push(e)
                })
            }
        }
    }
}
</script>
