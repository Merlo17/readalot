<template>
    <div
        id="app"
        class="flex flex-col gap-16 w-full mt-0 place-content-center place-items-center"
    >
        <NavigationBar />
        <router-view class="w-1/2"></router-view>
    </div>
</template>

<script setup lang="ts">
import NavigationBar from './components/NavigationBar.vue';
</script>

<style>
@tailwind base;
@tailwind components;
@tailwind utilities;

@import url('https://fonts.googleapis.com/css2?family=Roboto:ital,wght@0,300;0,400;0,500;1,300;1,400;1,500&display=swap');

#app {
    font-family: 'Roboto', sans-serif;
}
</style>
