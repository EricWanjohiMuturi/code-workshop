<script setup>
    import Heading from '@/components/Heading.vue';
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
<section class="min-h-screen flex items-center" data-aos="fade-up" data-aos-duration="1000">
    <div>
      <div class="grid grid-cols-1 sm:grid-cols-1 md:grid-cols-2 items-center gap-x-20">
        <div class="p-3">
            <Heading label="Reach out"/>
        </div>
      </div>
    </div>
</section>

</template>

<style scoped>

</style>