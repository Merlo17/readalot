<template>
    <div id="app">
        <PaperSwiper :papers="tmpPapers" />
    </div>
</template>

<script setup>
import PaperSwiper from './components/PaperSwiper.vue';
let tmpPapers = ['Slide 0', 'Slide 1', 'Slide 2'];
</script>

<style></style>
