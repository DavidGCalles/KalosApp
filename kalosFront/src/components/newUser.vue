<template>
	<div>
	  <h3>Register</h3>
	  <form @submit.prevent="register">
		<div>
		  <label for="username">Username:</label>
		  <input id="username" v-model="username" required>
		</div>
		<div>
		  <label for="password">Password:</label>
		  <input type="password" id="password" v-model="password" required>
		</div>
		<button type="submit">Register</button>
	  </form>
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
	  async register() {
		try {
		  const response = await axios.post('http://localhost:8000/users/', {
			username: this.username,
			password: this.password
		  });
		  alert('Registration successful');
		  console.log('Registration response:', response.data);
		  this.username = ''; // Clear the username
		  this.password = ''; // Clear the password
		} catch (error) {
		  alert('Registration failed');
		  console.error('Error during registration:', error);
		}
	  }
	}
  }
  </script>