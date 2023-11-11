<script setup lang="ts">
import { computed, onMounted } from 'vue';
import SearchInput from 'vue-search-input';
import 'vue-search-input/dist/styles.css';
import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome';

const props = defineProps(['modelValue']);
const emit = defineEmits(['update:modelValue', 'submitQuery']);

const showClearIcon = computed(() => props.modelValue.length > 0);

// onMounted(() => {
//     console.log(document.getElementsByClassName('search-icon search'));
//     document
//         .getElementsByClassName('search-icon search')[0]
//         .addEventListener('click', emit('click', props.modelValue), false);
// });

const clear = () => {
    emit('update:modelValue', '');
};

const submitQuery = () => {
    emit('submitQuery', props.modelValue);
};
</script>

<template>
    <div
        class="flex flex-row gap-3 px-2 py-1 bg-white rounded-md text-black"
        @keydown.space.enter="submitQuery"
    >
        <button class="w-6" @click="submitQuery">
            <font-awesome-icon :icon="['fas', 'magnifying-glass']" />
        </button>
        <input
            ref="inputRef"
            type="search"
            class="flex-grow bg-transparent outline-none"
            :value="modelValue"
            @input="emit('update:modelValue', $event.target.value)"
        />
        <button v-if="showClearIcon" :click="clear" class="w-6">
            <font-awesome-icon :icon="['fas', 'x']" />
        </button>
    </div>
</template>
