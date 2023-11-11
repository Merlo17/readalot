<script setup lang="ts">
import { ref, defineProps, Ref } from 'vue';
import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome';
let props = defineProps<{
    papers: Ref<string[]>;
}>();   

function like(paper) {
    paper.liked = true
}

</script>

<template>
    <div class="flex flex-col gap-6 place-items-center space-y-8 flex-1 sticky"> 
        <div v-for="(paper, index) in props.papers" :key="index"
        class="rounded overflow-hidden shadow-lg p-10 space-y-10 sticky w-[60vh] h-[80vh] flex flex-col justify-between bg-white">
        <div class="space-y-4">
            <div class="flex flex-row justify-center">
                <h1 class="text-4xl font-bold">{{ paper.title }}</h1>
            </div>
            <div class="flex flex-row justify-between">
                <h2 class="text-xl italic">{{paper.authors}}</h2>
                <h2 class="text-xl">{{paper.date}}</h2>
            </div>
        </div>
        <div class="flex">
            <p class="text-sm text-ellipsis overflow-hidden text-justify h-full">
                {{ paper.abstract }}
            </p>
        </div>
            
            <div class="flex justify-between">
                <div class="flex justify-between gap-6">
                     <button>
                        <font-awesome-icon
                            class="w-8 h-8"
                            v-bind:icon="['far', 'circle-xmark']"
                            color="#1E293B"
                        />
                    </button>
                    <button @click="like(paper)">
                        <font-awesome-icon
                            class="w-8 h-8"
                            v-bind:icon="paper.liked ? ['fas', 'heart'] : ['far', 'heart']"
                            v-bind="paper.liked ? { color: '#ff7477' } : { color: '#1E293B' }"
                        />
                    </button>

                </div>
                <a :href="paper.doi" class="text-blue-500 hover:underline">{{paper.doi}}</a>
            </div>        
        </div>
    </div>
</template>