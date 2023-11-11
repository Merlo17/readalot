<template>
    <main>
        <PaperSwiper :papers="tmpPapers" />
    </main>
</template>

<script setup lang="ts">
import { ref, reactive } from 'vue';
import QueryBar from '../components/QueryBar.vue';
import PaperSwiper from '../components/PaperSwiper.vue';

let query = ref('');
let tmpPapers = reactive([
    {
        title: 'Paper 1',
        date: '2021-01-01',
        authors: 'Author 1, Author 2',
        abstract:
            'Lorem ipsum dolor sit amet, qui minim labore adipisicing minim sint cillum sint consectetur cupidatat. Lorem ipsum dolor sit amet, qui minim labore adipisicing minim sint cillum sint consectetur cupidatat. Lorem ipsum dolor sit amet, qui minim labore adipisicing minim sint cillum sint consectetur cupidatat. Lorem ipsum dolor sit amet, qui minim labore adipisicing minim sint cillum sint consectetur cupidatat.',
        doi: 'https://doi.org/10.1109/ICCV.2019.00200',
    },
    {
        title: 'Paper 2',
        date: '2021-01-01',
        authors: 'Author 1, Author 2',
        abstract:
            'Lorem ipsum dolor sit amet, qui minim labore adipisicing minim sint cillum sint consectetur cupidatat. Lorem ipsum dolor sit amet, qui minim labore adipisicing minim sint cillum sint consectetur cupidatat. Lorem ipsum dolor sit amet, qui minim labore adipisicing minim sint cillum sint consectetur cupidatat. Lorem ipsum dolor sit amet, qui minim labore adipisicing minim sint cillum sint consectetur cupidatat.',
        doi: 'https://doi.org/10.1109/ICCV.2019.00200',
    },
    {
        title: 'Paper 3',
        date: '2021-01-01',
        authors: 'Author 1, Author 2',
        abstract:
            'Lorem ipsum dolor sit amet, qui minim labore adipisicing minim sint cillum sint consectetur cupidatat. Lorem ipsum dolor sit amet, qui minim labore adipisicing minim sint cillum sint consectetur cupidatat. Lorem ipsum dolor sit amet, qui minim labore adipisicing minim sint cillum sint consectetur cupidatat. Lorem ipsum dolor sit amet, qui minim labore adipisicing minim sint cillum sint consectetur cupidatat.',
        doi: 'https://doi.org/10.1109/ICCV.2019.00200',
    },
]);
</script>
