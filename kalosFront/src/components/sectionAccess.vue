<script setup>
	defineProps({
		title: {
			type: String,
			required: true
		},
		link: {
			type: String,
			required: true
		},
		desc: {
			type: String,
			required: true
		}
	})
</script>

<template>
<RouterLink :to="link"><h3>{{ title }}</h3></RouterLink>
<p>{{ desc }}</p>
</template>