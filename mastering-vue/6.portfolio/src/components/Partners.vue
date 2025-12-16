<script setup>
    import stejos from '@/assets/work/STEJOS-TOURS-TRAVEL.svg'
    import express from '@/assets/work/EXPRESSMARTKE_SHOPPING_ONLINE_2024.svg'
    import d4a from '@/assets/work/d4a.png'
    import info from '@/assets/work/infotech-logo.webp'
    import explore from '@/assets/work/explore.webp'
    import jepaks from '@/assets/work/jepaks.png'

    import { onMounted, nextTick } from 'vue'
    import AOS from 'aos'
    import 'aos/dist/aos.css'

    onMounted(async () => {
        await nextTick()
        AOS.init()
        AOS.refresh()
    })
</script>

<template>
<section class="my-20">
    <h2 class="text-center font-bold text-xl text-heading">Partnered/ Worked with</h2>
    <div class="grid grid-cols-2 sm:grid-cols-2 md:grid-cols-3 lg:grid-cols-6 xl:grid-cols-6 gap-10 items-center px-5">
        <div class="w-30" data-aos="fade-up" data-aos-duration="2000">
            <img :src="stejos" alt="">
        </div>
         <div class="w-30" data-aos="fade-up" data-aos-duration="2200">
            <img :src="express" alt="">
        </div>
         <div class="w-30" data-aos="fade-up" data-aos-duration="2400">
            <img :src="info" alt="">
        </div>
         <div class="w-40" data-aos="fade-up" data-aos-duration="2600">
            <img :src="d4a" alt="">
        </div>
         <div class="w-25" data-aos="fade-up" data-aos-duration="2800">
            <img :src="explore" alt="">
        </div>
         <div class="w-30" data-aos="fade-up" data-aos-duration="3000">
            <img :src="jepaks" alt="">
        </div>
    </div>
</section>
</template>

<style>

</style>