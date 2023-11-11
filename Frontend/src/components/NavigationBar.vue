<template>
    <main
        class="text-white flex flex-row justify-between w-full py-4 px-8 bg-slate-800 place-items-center"
    >
        <div class="w-1/3 justify-start">
            <img src="../assets/img/logo_white.png" class="h-16" alt="Logo" />
        </div>
        <div class="w-1/3 justify-center">
            <QueryBar v-model="query" />
        </div>
        <div class="w-1/3 flex justify-end">
            <img
                src="../assets/img/profile.jpg"
                class="rounded-full w-16 h-16"
                alt="Profile"
            />
        </div>
    </main>
</template>

<script setup lang="ts">
import QueryBar from '../components/QueryBar.vue';
</script>
