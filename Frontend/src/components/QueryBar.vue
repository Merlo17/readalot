<script setup lang="ts">
import { computed } from 'vue';
import SearchInput from 'vue-search-input';
import 'vue-search-input/dist/styles.css';

const props = defineProps(['modelValue']);
const emit = defineEmits(['update:modelValue']);

const query = computed({
    get() {
        return props.modelValue;
    },
    set(value) {
        emit('update:modelValue', value);
    },
});
</script>

<template>
    <search-input v-model="query" />
</template>
