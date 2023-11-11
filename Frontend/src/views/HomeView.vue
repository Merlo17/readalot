<template>
    <main
        class="flex flex-col gap-16 w-full mt-0 place-content-center place-items-center"
    >
        <NavigationBar :onSubmitQuery="sendQuery(query)" />
        <PaperSwiper class="w-1/2" :paper="ref(tmpPapers[0])" />
    </main>
</template>

<script setup lang="ts">
import { ref, reactive } from 'vue';
import NavigationBar from '../components/NavigationBar.vue';
import PaperSwiper from '../components/PaperSwiper.vue';
import ApiService from '@/services/ApiService';

async function sendQuery(query: string) {
    try {
        const { data } = await ApiService.browse({ query: query });
    } catch (err) {
        // uh oh
        console.log(err);
    }
}

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
