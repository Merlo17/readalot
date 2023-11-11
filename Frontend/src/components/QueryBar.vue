<script setup lang="ts">
import { computed, onMounted } from 'vue';
import SearchInput from 'vue-search-input';
import 'vue-search-input/dist/styles.css';

const props = defineProps(['modelValue']);
const emit = defineEmits(['update:modelValue', 'onClick']);

const query = computed({
    get() {
        return props.modelValue;
    },
    set(value) {
        emit('update:modelValue', value);
    },
});

onMounted(() => {
    document
        .getElementsByClassName('search-icon search')[0]
        .addEventListener('click', emit('onClick', query.value), false);
});
</script>

<template>
    <search-input v-model="query" />
</template>
