<script setup lang="ts">
import { ref, defineProps, Ref } from 'vue';
import { Swiper, SwiperSlide } from 'swiper/vue';
import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome';
import ApiService from '@/services/ApiService';

// Import Swiper styles
import 'swiper/css';
import 'swiper/css/effect-cards';

// Import required modules
import { EffectCards } from 'swiper/modules';

const ANIMATION_DURATION = 100;

let props = defineProps<{
    paper: Ref<any>;
}>();
let dummyPaper = {
    title: '',
    authors: '',
    date: '',
    abstract: '',
};
let visiblePapers = ref([dummyPaper, props.paper.value, dummyPaper]);

const modules = [EffectCards];

let swiperRef: any = null;
function setSwiperRef(swiper: any) {
    swiperRef = swiper;
    swiperRef.activeIndex = 1;
    swiperRef.update();
}

function updateList(data: any) {
    swiperRef.activeIndex = 1;

    props.paper.value = data;
    visiblePapers.value = [dummyPaper, props.paper.value, dummyPaper];

    swiperRef.update();
}

async function swipeLeft() {
    swiperRef.translateTo(
        swiperRef.getTranslate() + swiperRef.width,
        ANIMATION_DURATION,
    );

    try {
        const { data } = await ApiService.swipe({ swipeDirection: 'left' });
        setTimeout(function () {
            updateList(data);
        }, ANIMATION_DURATION);
    } catch (err) {
        // uh oh
        let data = props.paper.value;
        setTimeout(function () {
            updateList(data);
        }, ANIMATION_DURATION);

        console.log(err);
    }
}

async function swipeRight() {
    swiperRef.translateTo(
        swiperRef.getTranslate() - swiperRef.width,
        ANIMATION_DURATION,
    );

    try {
        const { data } = await ApiService.swipe({ swipeDirection: 'right' });
        setTimeout(function () {
            updateList(data);
        }, ANIMATION_DURATION);
    } catch (err) {
        // uh oh
        let data = props.paper.value;
        setTimeout(function () {
            updateList(data);
        }, ANIMATION_DURATION);

        console.log(err);
    }
}
</script>

<template>
    <div>
        <swiper
            :effect="'cards'"
            :grabCursor="true"
            :modules="modules"
            :allowTouchMove="false"
            :observer="true"
            :observeSlideChildren="true"
            :observeParents="true"
            @swiper="setSwiperRef"
            class="w-[500px] h-[600px]"
        >
            <swiper-slide v-for="(paper, index) in visiblePapers" :key="index">
                <div class="swiper-slide">
                    <div class="flex flex-col gap-8 mt-20 m-10">
                        <h1 class="font-bold text-4xl">{{ paper.title }}</h1>
                        <div class="flex flex-row justify-between italic">
                            <p>{{ paper.authors }}</p>
                            <p>{{ paper.date }}</p>
                        </div>
                        <p class="text-ellipsis text-justify">
                            {{ paper.abstract }}
                        </p>
                    </div>
                </div>
            </swiper-slide>
        </swiper>

        <div class="buttons">
            <button @click="swipeLeft">
                <font-awesome-icon
                    :icon="['fas', 'circle-xmark']"
                    class="swipe-button"
                />
            </button>
            <button @click="swipeRight">
                <font-awesome-icon
                    :icon="['fas', 'heart']"
                    class="swipe-button"
                />
            </button>
        </div>
    </div>
</template>

<style scoped>
@tailwind base;
@tailwind components;
@tailwind utilities;
#app {
    height: 100%;
}
html,
body {
    position: relative;
    height: 100%;
}

body {
    background: #eee;
    font-family:
        Helvetica Neue,
        Helvetica,
        Arial,
        sans-serif;
    font-size: 14px;
    color: #000;
    margin: 0;
    padding: 0;
}

.swipe-button {
    font-size: 60px;
    padding: 1rem;
    color: #082235;
}

.buttons {
    display: flex;
    justify-content: center;
    align-items: center;
    margin: 0 10px;
}

body {
    background: #fff;
    font-size: 14px;
    color: #000;
    margin: 0;
    padding: 0;
}

html,
body {
    position: relative;
    height: 100%;
}

.swiper-slide {
    display: flex;
    border-radius: 18px;
    color: #082235;
    background: #d7e3fc;
}
</style>
