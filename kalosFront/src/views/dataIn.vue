<script setup>
	import InputNumber from 'primevue/inputnumber'
	import Calendar from 'primevue/calendar';
	import Fieldset from 'primevue/fieldset';
	import Button from 'primevue/button';
	import { ref } from 'vue';
	const weight = ref(0)
	const medidas = ref({
		antebrazo : 10,
		biceps: 0
	})
</script>

<template>
	<h2>¡Introduce tus datos para el día de hoy!</h2>
	<div class="fieldSetContainer">
		<Fieldset legend="Fecha" style="width: 49%;">
			<Calendar v-model="date" />
		</Fieldset>
		<Fieldset legend="Peso (en Kg)" style="width: 49%;">
			<InputNumber v-model="weight" inputID="weightInput" :min="0" :step="0.1"/>
		</Fieldset>
	</div>
	<Fieldset legend="Medidas Corporales (en Cm)" style="width: 100%;">
		<div class="fieldSetContainer">
			<Fieldset legend="Biceps" style=""><InputNumber class="w-min" v-model="medidas['biceps']" inputID="bicepsInput" :min="0" :step="0.1"/></Fieldset>
			<Fieldset legend="Antebrazos" style=""><InputNumber class="w-min" v-model="medidas['biceps']" inputID="bicepsInput" :min="0" :step="0.1"/></Fieldset>
			<Fieldset legend="Pecho" style=""><InputNumber class="w-min" v-model="medidas['biceps']" inputID="bicepsInput" :min="0" :step="0.1"/></Fieldset>
			<Fieldset legend="Bajo Pecho" style=""><InputNumber class="w-min" v-model="medidas['biceps']" inputID="bicepsInput" :min="0" :step="0.1"/></Fieldset>
			<Fieldset legend="Cintura" style=""><InputNumber class="w-min" v-model="medidas['biceps']" inputID="bicepsInput" :min="0" :step="0.1"/></Fieldset>
			<Fieldset legend="Bajo Tripa" style=""><InputNumber class="w-min" v-model="medidas['biceps']" inputID="bicepsInput" :min="0" :step="0.1"/></Fieldset>
			<Fieldset legend="Cadera" style=""><InputNumber class="w-min" v-model="medidas['biceps']" inputID="bicepsInput" :min="0" :step="0.1"/></Fieldset>
			<Fieldset legend="Muslo" style=""><InputNumber class="w-min" v-model="medidas['biceps']" inputID="bicepsInput" :min="0" :step="0.1"/></Fieldset>
			<Fieldset legend="Encima Rodilla" style=""><InputNumber class="w-min" v-model="medidas['biceps']" inputID="bicepsInput" :min="0" :step="0.1"/></Fieldset>
			<Fieldset legend="Gemelo" style=""><InputNumber class="w-min" v-model="medidas['biceps']" inputID="bicepsInput" :min="0" :step="0.1"/></Fieldset>
		</div>
	</Fieldset>
	<Button label="Enviar"></Button>
</template>
<!--			Cadera	Muslo	Encima Rodilla	Gemelo-->

<style>
.fieldSetContainer{
	display:flex;
	flex-wrap: wrap;
	gap: 20px;
}

</style>