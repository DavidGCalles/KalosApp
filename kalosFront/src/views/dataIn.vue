<script setup>
	import InputNumber from 'primevue/inputnumber'
	import Fieldset from 'primevue/fieldset';
	import { ref } from 'vue';
	const weight = ref(0)
</script>

<template>
	<h1>¡Introduce tus datos para el día de hoy!</h1>
	 <Fieldset legend="Peso (en Kg)" style="display: flex; justify-content: center; align-items: center; width: 50%;">
		<InputNumber v-model="weight" inputID="weightInput" showButtons buttonLayout="vertical" :min="0" :step="0.1"/>
	</Fieldset>
</template>