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
            class="w-[550px] h-[700px]"
        >
            <swiper-slide v-for="(paper, index) in visiblePapers" :key="index">
                <div
                    class="rounded overflow-hidden p-10 space-y-10 sticky flex flex-col justify-between bg-white"
                >
                    <div class="space-y-4">
                        <div class="flex flex-row justify-center">
                            <h1 class="text-2xl font-bold">
                                {{ paper.title }}
                            </h1>
                        </div>
                        <div class="flex flex-row justify-between">
                            <h2 class="text-xl italic">{{ paper.authors }}</h2>
                            <h2 class="text-xl">{{ paper.date }}</h2>
                        </div>
                    </div>
                    <div class="flex">
                        <p
                            class="text-sm text-ellipsis overflow-hidden text-justify h-full line-clamp [24]"
                        >
                            {{ paper.abstract }}
                        </p>
                    </div>

                    <div class="flex justify-between">
                        <div class="flex justify-between gap-6">
                            <button @click="swipeLeft">
                                <font-awesome-icon
                                    class="w-8 h-8"
                                    v-bind:icon="['far', 'circle-xmark']"
                                    color="#1E293B"
                                />
                            </button>
                            <button @click="swipeRight">
                                <font-awesome-icon
                                    class="w-8 h-8"
                                    v-bind:icon="
                                        paper.liked
                                            ? ['fas', 'heart']
                                            : ['far', 'heart']
                                    "
                                    v-bind="
                                        paper.liked
                                            ? { color: '#ff7477' }
                                            : { color: '#1E293B' }
                                    "
                                />
                            </button>
                        </div>
                        <a
                            :href="paper.doi"
                            class="text-blue-500 hover:underline"
                            >{{ paper.doi }}</a
                        >
                    </div>
                </div>
            </swiper-slide>
        </swiper>
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

.buttons {
    display: flex;
    justify-content: center;
    align-items: center;
    margin: 0 10px;
}

.swiper-slide {
    display: flex;
    border-radius: 18px;
    color: #082235;
    background: #ffffff;
}
</style>
