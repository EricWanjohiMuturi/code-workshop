<script setup>
import Heading from './Heading.vue'
import BlogsCard from './BlogsCard.vue'
import { onMounted, nextTick } from 'vue'
import AOS from 'aos'
import 'aos/dist/aos.css'

onMounted(async () => {
await nextTick()
AOS.init()
AOS.refresh()
})
const blogs = [
  {
    id: 1,
    title: 'Pip vs. UV: A Deep Dive into Python Package Management & Tooling.',
    category: ['Pip', 'uv', 'Python'],
    url: 'https://medium.com/@emuturi124/pip-vs-uv-a-deep-dive-into-python-package-management-tooling-b21d0cd1404b',
  },
  {
    id: 2,
    title: 'Why Companies are Moving to the Cloud: A Kenyan Perspective',
    category: ['cloud', 'servers'],
    url: 'https://medium.com/@emuturi124/why-companies-are-moving-to-the-cloud-a-global-and-kenyan-perspective-48073d8f81d7',
  },
  {
    id: 3,
    title: 'Unmasking the Hidden Costs of Technical Debt in the Vibe Coding Era',
    category: ['Technical Debt', 'ai', 'vibe coding'],
    url: 'https://medium.com/@emuturi124/unmasking-the-hidden-costs-of-technical-debt-f11d1224d61f',
  },
  {
    id: 4,
    title: 'Requirements for M-Pesa Online Payment Setup in Kenya (2025 Guide)',
    category: ['mpesa', 'paybill', 'till', 'daraja'],
    url: 'https://jepaks.systems/blogs/requirements-for-m-pesa-online-payment-setup-in-kenya-2025-guide',
  },
]
</script>

<template>
  <div data-aos="fade-up" data-aos-duration="1000">
    <Heading label="Documenting my experiences..." />
    <h3 class="text-xl mb-5" data-aos="fade-up" data-aos-duration="1200">Find out what I have been up to lately</h3>

    <div class="grid grid-cols-1 md:grid-cols-2 gap-x-20 gap-y-6" data-aos="fade-up" data-aos-duration="1600">
      <BlogsCard
        v-for="blog in blogs"
        :key="blog.id"
        :heading="blog.title"
        :url = "blog.url"
        :category="blog.category"
      />
    </div>
  </div>
</template>

<style scoped>

</style>