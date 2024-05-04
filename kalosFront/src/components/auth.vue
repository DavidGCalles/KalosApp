<template>
	<div>
	  <input v-model="username" placeholder="Username">
	  <input type="password" v-model="password" placeholder="Password">
	  <button @click="login">Login</button>
	</div>
  </template>
  
  <script>
  import axios from 'axios';
  
  export default {
	data() {
	  return {
		username: '',
		password: ''
	  };
	},
	methods: {
		async login() {
      try {
        // Usando URLSearchParams para codificar los datos correctamente
        const formData = new URLSearchParams();
        formData.append('username', this.username);
        formData.append('password', this.password);

        const response = await axios.post('http://localhost:8000/token', formData, {
          headers: {
            'Content-Type': 'application/x-www-form-urlencoded'
          }
        });
        console.log('Logged in:', response.data);
        // Aquí puedes manejar acciones post-login, como almacenar el token, etc.
      } catch (error) {
        console.error('Error logging in:', error.response ? error.response.data : error);
      }
    }
	}
  }
  </script>