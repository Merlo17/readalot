<template>
    <main
        class="flex flex-col gap-16 w-full mt-0 place-content-center place-items-center"
    >
        <NavigationBar @submitQuery="sendQuery" />
        <PaperSwiper class="w-1/2" :paper="ref(papers[0])" />
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
        papers = data;
    } catch (err) {
        // uh oh
        console.log(err);
    }
}

let query = ref('');
// let papers = ref([]);
let papers = reactive([
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
            'The dominant sequence transduction models are based on complex recurrent or convolutional neural networks that include an encoder and a decoder. The best performing models also connect the encoder and decoder through an attention mechanism. We propose a new simple network architecture, the Transformer, based solely on attention mechanisms, dispensing with recurrence and convolutions entirely. Experiments on two machine translation tasks show these models to be superior in quality while being more parallelizable and requiring significantly less time to train. Our model achieves 28.4 BLEU on the WMT 2014 English to-German translation task, improving over the existing best results, including ensembles, by over 2 BLEU. On the WMT 2014 English-to-French translation task, our model establishes a new single-model state-of-the-art BLEU score of 41.8 after training for 3.5 days on eight GPUs, a small fraction of the training costs of the best models from the literature. We show that the Transformer generalizes well to other tasks by applying it successfully to English constituency parsing both with large and limited training data. The dominant sequence transduction models are based on complex recurrent or convolutional neural networks that include an encoder and a decoder. The best performing models also connect the encoder and decoder through an attention mechanism. We propose a new simple network architecture, the Transformer, based solely on attention mechanisms, dispensing with recurrence and convolutions entirely. Experiments on two machine translation tasks show these models to be superior in quality while being more parallelizable and requiring significantly less time to train. Our model achieves 28.4 BLEU on the WMT 2014 English to-German translation task, improving over the existing best results, including ensembles, by over 2 BLEU. On the WMT 2014 English-to-French translation task, our model establishes a new single-model state-of-the-art BLEU score of 41.8 after training for 3.5 days on eight GPUs, a small fraction of the training costs of the best models from the literature. We show that the Transformer generalizes well to other tasks by applying it successfully to English constituency parsing both with large and limited training data.',
        doi: 'https://doi.org/10.1109/ICCV.2019.00200',
    },
]);
</script>
