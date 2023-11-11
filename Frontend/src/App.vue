<template>
    <div id="app">
        <QueryBar v-model="query" />
        <PaperSwiper :papers="tmpPapers" />
    </div>
</template>

<script setup>
import { ref, reactive } from 'vue';
import QueryBar from './components/QueryBar.vue';
import PaperSwiper from './components/PaperSwiper.vue';

let query = ref('');
let tmpPapers = reactive(['Slide 0', 'Slide 1', 'Slide 2']);
</script>

<style></style>
