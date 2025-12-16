<script setup lang="ts">
  import src from '@/assets/Muturi_Eric_Full-Stack_Developer.png'
  import Outlinebtn from './Outlinebtn.vue';
  import Filledbtn from './Filledbtn.vue';

</script>

<template>
  <section class="min-h-screen flex items-center">
    <div class="grid grid-cols-1 sm:grid-cols-1 md:grid-cols-2 items-center gap-x-20">
      <div class="p-3">
        <h2 class="font-medium text-6xl my-10">Get to know me first...</h2>
        <div class="mb-5">
          <p>Hello there</p>
          <h1 class="font-medium text-2xl">Muturi Eric Wanjohi</h1>
        </div>
        <div class="mb-5">
          <p>
            All my life I have never been this passionate about solving problems with software. Have you identified a gap in your business? 
            Do you want to automate processes and tasks? Need me to join your team? I am your go to software guy.
  
          </p>
          <p>
            I specialize in Software Development and Automations. I deliver responsive, scalable , secure and user-centric solutions. 
            Let's transform your ideas into powerful web applications designed for impact and performance.
          </p>
        </div>
        <div class="flex items-center gap-5"> 
          <Outlinebtn />
          <Filledbtn />
        </div>
      </div>
      <div class="flex justify-center">
        <img :src width="500" alt="">
      </div>
    </div>
  </section>
</template>

<style scoped>

</style>
