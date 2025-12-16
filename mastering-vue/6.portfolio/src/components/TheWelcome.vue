<script setup>
  import eric from '@/assets/Muturi_Eric_Full-Stack_Developer.png'
  import Outlinebtn from './Outlinebtn.vue';
  import Filledbtn from './Filledbtn.vue';
  import Partners from './Partners.vue';

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
  <section id="hero" class="min-h-screen flex items-center" data-aos="fade-up" data-aos-duration="1000">
    <div>
      <div class="grid grid-cols-1 sm:grid-cols-1 md:grid-cols-2 items-center gap-x-20">
        <div class="p-3">
          <h2 class="font-medium text-4xl sm:text-4xl md:text-5xl lg:text-6xl my-10 text-heading" data-aos="fade-up" data-aos-duration="1000">Get to know me first...</h2>
          <div class="mb-5" data-aos="fade-up" data-aos-duration="1500" >
            <p class="text-sm">Hello there 👋, I'm</p>
            <h1 class="font-medium text-2xl text-heading">Muturi Eric Wanjohi</h1>
          </div>
          <div class="mb-10">
            <p data-aos="fade-up" data-aos-duration="1700">
              All my life I have never been this passionate about solving problems with software. Have you identified a gap in your business? 
              Do you want to automate processes and tasks? Need me to join your team? I am your go to software guy.
    
            </p>
            <p data-aos="fade-up" data-aos-duration="1900">
              I specialize in Software Development and Automations. I deliver responsive, scalable , secure and user-centric solutions. 
              Let's transform your ideas into powerful web applications designed for impact and performance.
            </p>
          </div>
          <div class="flex items-center gap-5" data-aos="fade-up" data-aos-duration="2200"> 
            <Outlinebtn />
            <Filledbtn />
          </div>
        </div>
        <div class="flex justify-center p-5">
          <div class="relative inline-block" data-aos="fade-up" data-aos-duration="2200">
            <!-- Pulse -->
            <div class="absolute top-2 right-2 sm:top-3 sm:right-3 lg:top-4 lg:right-4 z-10">
              <div class="flex h-10 w-10 items-center justify-center">
                <span
                  class="absolute inline-flex h-full w-full animate-ping rounded-full bg-green-400 opacity-75"
                ></span>
                <span
                  class="relative inline-flex h-4 w-20 items-center justify-center rounded-full text-[10px] font-bold text-center backdrop-blur"
                >
                  Available For Hire
                </span>
              </div>
            </div>
            <!-- End pulse -->

            <img :src="eric" width="500" alt="" class="block" />
          </div>

        </div>
      </div>
      <div data-aos="fade-up" data-aos-duration="2600">
        <Partners />
      </div>
    </div>
  </section>
</template>

<style scoped>

</style>
