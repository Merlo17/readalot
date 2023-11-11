<script setup lang="ts">
import PaperSwiper from '../components/PaperSwiper.vue';
let tmpPapers = ['Slide 1', 'Slide 2'];
</script>

<template>
    <main>
        <PaperSwiper :papers="tmpPapers" />
    </main>
</template>
