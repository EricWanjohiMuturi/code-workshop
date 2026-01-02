<script setup>
    import Skills from '@/components/Skills.vue';
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
      <div class="p-3" data-aos="fade-up" data-aos-duration="1250">
        <Skills />
      </div>
    </div>
</section>

</template>

<style scoped>

</style>
