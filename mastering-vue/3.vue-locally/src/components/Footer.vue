<script setup>
    import {ref} from 'vue'
    const year = ref('2025')
</script>

<template>
    <footer>
        <p>&copy; <span class="year">{{ year }}</span> </p>
    </footer>
</template>

<style scoped>
  footer {
      position:fixed;
      bottom:0;
      padding-bottom:20px;
  }
  .year{
    color: blue;
  }
</style>