<script setup lang="ts">
import { ref, defineProps } from 'vue';
import { Swiper, SwiperSlide } from 'swiper/vue';
import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome';

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
        <div class="buttons">
            <button @click="swipeLeft">
                <font-awesome-icon :icon="['fas', 'circle-xmark']"  class="swipe-button" />
            </button>
            <button @click="swipeRight">
                <font-awesome-icon :icon="['fas', 'heart']" class="swipe-button" />
            </button>
        </div>
        <!-- Pagination -->
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

#app {
    display: flex;
    justify-content: center;
    align-items: center;
}

.swiper {
    width: 500px;
    height: 800px;
}

.swiper-slide {
    display: flex;
    align-items: center;
    justify-content: center;
    border-radius: 18px;
    font-size: 22px;
    font-weight: bold;
    color: #082235;
    background: #d7e3fc;
}
.center {
  margin: auto;
  width: 50%;
  padding: 10px;
}
</style>
