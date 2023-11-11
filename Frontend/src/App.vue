<template>
    <div
        id="app"
        class="flex flex-col mt-0 pt-0 place-items-center bg-slate-100 h-screen w-screen"
    >
        <NavigationBar />
        <router-view class="w-1/2"></router-view>
    </div>
</template>

<style>
@tailwind base;
@tailwind components;
@tailwind utilities;

@import url('https://fonts.googleapis.com/css2?family=Roboto:ital,wght@0,300;0,400;0,500;1,300;1,400;1,500&display=swap');

#app {
    font-family: 'Roboto', sans-serif;
}
</style>
