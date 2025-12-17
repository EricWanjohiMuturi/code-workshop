<script setup lang="ts">
defineProps<{
  heading: string
  category: string[]
  url: string
}>()
</script>

<template>
  <a :href="url" target="_blank">
    <div class="card shadow-lg shadow-[#3d5690]/30">
      <div class="main-content">
        <p class="heading">
          {{ heading }}
        </p>

        <div class="categories">
          <span
            v-for="(cat, index) in category"
            :key="index"
          >
            {{ cat }}
          </span>
        </div>
      </div>
    </div>
  </a>
</template>

<style scoped>
.card {
  width: 330px;
  padding: 20px;
  color: #3d5690;
  background: linear-gradient(#edebdf, #edebdf) padding-box,
    linear-gradient(145deg, transparent 35%, #6ecbe2, #3d5690) border-box;
  border: 2px solid transparent;
  border-radius: 8px;
  display: flex;
  flex-direction: column;
  cursor: pointer;
  transform-origin: top bottom;
  transition: all 0.8s cubic-bezier(0.23, 1, 0.32, 1);
}

.card .main-content {
  flex: 1;
}


.card .heading {
  font-size: 24px;
  margin: 24px 0 16px;
  font-weight: 600;
}

.card .categories {
  display: flex;
  gap: 10px;
}

.card .categories span {
  background-color: #3d5690;
  color: #edebdf;
  padding: 4px 8px;
  font-weight: 600;
  text-transform: uppercase;
  font-size: 12px;
  border-radius: 50em;
}


.card:hover {
  rotate: -6deg;
}


</style>