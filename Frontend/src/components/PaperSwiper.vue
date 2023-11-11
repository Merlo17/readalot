<script setup lang="ts">
import { ref, defineProps } from 'vue';
import { Swiper, SwiperSlide } from 'swiper/vue';

// Import Swiper styles
import 'swiper/css';
import 'swiper/css/effect-cards';
// import './assets/swiper.css';

// Import required modules
import { EffectCards } from 'swiper/modules';

let props = defineProps<{
    papers: string[];
}>();
let visiblePapers = ref([props.papers[1], props.papers[0], props.papers[1]]);
let currPaperIdx = 0;

const modules = [EffectCards];

let swiperRef: any = null;
function setSwiperRef(swiper: any) {
    swiperRef = swiper;
    swiperRef.activeIndex = 1;
    swiperRef.update();
}

function updateList() {
    swiperRef.activeIndex = 1;

    currPaperIdx = (currPaperIdx + 1) % props.papers.length;
    visiblePapers.value = [
        props.papers[(currPaperIdx + 1) % props.papers.length],
        props.papers[currPaperIdx],
        props.papers[(currPaperIdx + 1) % props.papers.length],
    ];

    swiperRef.update();
}

function swipeLeft() {
    swiperRef.translateTo(swiperRef.getTranslate() + swiperRef.width, 100);
    setTimeout(function () {
        updateList();
    }, 100);
}

function swipeRight() {
    swiperRef.translateTo(swiperRef.getTranslate() - swiperRef.width, 100);
    setTimeout(function () {
        updateList();
    }, 100);

    // TODO: Update papers from server (with new query if liked)
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
            class="mySwiper"
            @swiper="setSwiperRef"
        >
            <swiper-slide v-for="(paper, index) in visiblePapers" :key="index">
                <div class="swiper-slide">
                    <div class="paper">
                        <h1>{{ paper }}</h1>
                        <h3>Some text</h3>
                    </div>
                </div>
            </swiper-slide>
        </swiper>

        <!-- Buttons -->
        <button class="swiper-button-prev" :onClick="swipeLeft">Prev</button>
        <button class="swiper-button-next" :onClick="swipeRight">Next</button>
        <!-- Pagination -->
    </div>
</template>

<style scoped>
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

body {
    background: #fff;
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

html,
body {
    position: relative;
    height: 100%;
}

#app {
    display: flex;
    justify-content: center;
    align-items: center;
}

.swiper {
    width: 240px;
    height: 320px;
}

.swiper-slide {
    display: flex;
    align-items: center;
    justify-content: center;
    border-radius: 18px;
    font-size: 22px;
    font-weight: bold;
    color: #fff;
}

.swiper-slide:nth-child(1n) {
    background-color: rgb(206, 17, 17);
}

.swiper-slide:nth-child(2n) {
    background-color: rgb(0, 140, 255);
}

.swiper-slide:nth-child(3n) {
    background-color: rgb(10, 184, 111);
}

.swiper-slide:nth-child(4n) {
    background-color: rgb(211, 122, 7);
}

.swiper-slide:nth-child(5n) {
    background-color: rgb(118, 163, 12);
}

.swiper-slide:nth-child(6n) {
    background-color: rgb(180, 10, 47);
}

.swiper-slide:nth-child(7n) {
    background-color: rgb(35, 99, 19);
}

.swiper-slide:nth-child(8n) {
    background-color: rgb(0, 68, 255);
}

.swiper-slide:nth-child(9n) {
    background-color: rgb(218, 12, 218);
}

.swiper-slide:nth-child(10n) {
    background-color: rgb(54, 94, 77);
}
</style>
