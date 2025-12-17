<script setup>
  import Hero from '@/components/Hero.vue'
  import Blogs from '@/components/Blogs.vue';
  import PlaylistCard from '@/components/PlaylistCard.vue';
</script>

<template>
  <main>
    <Hero />
    <div class="grid grid-cols-1 sm:grid-cols-1 md:grid-cols-2 items-center gap-x-20 mb-20">
      <Blogs />
      <PlaylistCard />
    </div>
  </main>
</template>
