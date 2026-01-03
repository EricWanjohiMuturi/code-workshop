<script setup lang="ts">
import { computed } from 'vue'

const props = defineProps<{
  link: string
  image: string
  industry?: string
  date?: string | number
  projectname?: string
  tech?: string | string[]
}>()

const techList = computed(() => {
  const t = props.tech ?? []
  if (Array.isArray(t)) return t
  return typeof t === 'string'
    ? t.split(',').map(s => s.trim()).filter(Boolean)
    : []
})
</script>

<template>
  <a
    :href="link"
    class="w-96 hover:scale-105 transition-transform duration-300 group p-5"
    target="_blank"
  >
    <figure class="overflow-hidden rounded-lg relative mb-1">
      <img :src="image" :alt="projectname" class="object-cover object-center aspect-video bg-gray-400" />
      <span v-if="industry" class="absolute top-2 left-2 px-3 py-1 bg-green-600 backdrop-blur-sm text-xs rounded-full text-gray-50">
        {{ industry }}
      </span>
    </figure>

    <time v-if="date" datetime="2025-02-17T19:10:07.818Z" class="text-xs text-eric">
      Completed on: <span>⦁</span> {{ date }}
    </time>

    
    <p class="text-xl text-eric mt-2 text-gray-50">
      {{ projectname }}
    </p>

    <div class="flex flex-wrap gap-2 mt-3">
      <span v-for="(t, i) in techList" :key="i" class="px-3 py-1 bg-eric rounded-full text-xs text-gray-50">
        {{ t }}
      </span>
    </div>

  </a>
</template>