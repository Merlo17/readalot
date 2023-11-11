<template>
    <main
        class="text-white flex flex-row justify-between w-full py-2 px-4 bg-slate-800"
    >
        <div class="flex flex-row gap-2">
            <p>Logo</p>
            <p class="font-bold">PaperMatch</p>
        </div>
        <div class="w-1/4">
            <QueryBar v-model="query" />
        </div>
        <p>Account pic</p>
    </main>
</template>

<script setup lang="ts">
import QueryBar from '../components/QueryBar.vue';
</script>
