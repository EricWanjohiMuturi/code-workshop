<script setup>
import { ref, onMounted, onUnmounted, nextTick } from 'vue'

const isHidden = ref(false)
let lastScrollY = window.scrollY

const handleScroll = () => {
  const currentScrollY = window.scrollY

  if (currentScrollY > lastScrollY && currentScrollY > 60) {
    isHidden.value = true
  } else {
    isHidden.value = false
  }

  lastScrollY = currentScrollY
}

onMounted(() => {
  window.addEventListener('scroll', handleScroll, { passive: true })
})

onUnmounted(() => {
  window.removeEventListener('scroll', handleScroll)
})

</script>

<template>
  <div
    :class="[
      'fixed bottom-4 left-1/2 -translate-x-1/2 z-50 float-animation',
      'flex items-center justify-between gap-5 sm:gap-5 md:gap-5 lg:gap-8 xl:gap-10',
      'bg-[#edebdf] border border-gray-300 bg-opacity-80 backdrop-blur-md',
      'rounded-full px-6 py-3 shadow-xl shadow-[#3d5690]/30',
      'max-w-md w-fit',
      'transition-all duration-300 ease-in-out',
      'hover:shadow-xl hover:bg-opacity-90',
      isHidden ? 'translate-y-24 opacity-0' : 'translate-y-0 opacity-100'
    ]"
  >
    <!-- Button 1 -->
     <RouterLink to="/">
       <button
         class=" mx-2
                transition-transform duration-200 ease-in-out
                hover:scale-110 cursor-pointer"
       >
   
       <div>
         <div class="flex items-center justify-center">
           <svg class="w-4 h-4" viewBox="0 0 512 512" version="1.1" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" fill="#000000"><g id="SVGRepo_bgCarrier" stroke-width="0"></g><g id="SVGRepo_tracerCarrier" stroke-linecap="round" stroke-linejoin="round"></g><g id="SVGRepo_iconCarrier"> <title>about</title> <g id="Page-1" stroke="none" stroke-width="1" fill="none" fill-rule="evenodd"> <g id="about-white" fill="#3D5690" transform="translate(42.666667, 42.666667)"> <path d="M213.333333,3.55271368e-14 C95.51296,3.55271368e-14 3.55271368e-14,95.51168 3.55271368e-14,213.333333 C3.55271368e-14,331.153707 95.51296,426.666667 213.333333,426.666667 C331.154987,426.666667 426.666667,331.153707 426.666667,213.333333 C426.666667,95.51168 331.154987,3.55271368e-14 213.333333,3.55271368e-14 Z M213.333333,384 C119.227947,384 42.6666667,307.43872 42.6666667,213.333333 C42.6666667,119.227947 119.227947,42.6666667 213.333333,42.6666667 C307.44,42.6666667 384,119.227947 384,213.333333 C384,307.43872 307.44,384 213.333333,384 Z M240.04672,128 C240.04672,143.46752 228.785067,154.666667 213.55008,154.666667 C197.698773,154.666667 186.713387,143.46752 186.713387,127.704107 C186.713387,112.5536 197.99616,101.333333 213.55008,101.333333 C228.785067,101.333333 240.04672,112.5536 240.04672,128 Z M192.04672,192 L234.713387,192 L234.713387,320 L192.04672,320 L192.04672,192 Z" id="Shape"> </path> </g> </g> </g></svg>
         </div>
         <h6 class="text-xs font-medium text-indigo-900 mt-1">About</h6>
       </div>
       
       </button>
     </RouterLink>

    <!-- Button 2 -->
     <RouterLink to="/skills">
       <button
         class=" mx-2
                transition-transform duration-200 ease-in-out
                hover:scale-110 cursor-pointer"
       >
       
       <div>
         <div class="flex items-center justify-center">
           <svg class="w-4 h-4" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg"><g id="SVGRepo_bgCarrier" stroke-width="0"></g><g id="SVGRepo_tracerCarrier" stroke-linecap="round" stroke-linejoin="round"></g><g id="SVGRepo_iconCarrier"> <path d="M14.9615 5.27473C15.1132 4.7437 14.8058 4.19021 14.2747 4.03849C13.7437 3.88677 13.1902 4.19426 13.0385 4.72529L9.03847 18.7253C8.88675 19.2563 9.19424 19.8098 9.72528 19.9615C10.2563 20.1133 10.8098 19.8058 10.9615 19.2747L14.9615 5.27473Z" fill="#3d5690"></path> <path d="M5.7991 7.39879C6.13114 7.84012 6.04255 8.46705 5.60123 8.7991L2.40894 11.2009C1.87724 11.601 1.87723 12.399 2.40894 12.7991L5.60123 15.2009C6.04255 15.533 6.13114 16.1599 5.7991 16.6012C5.46705 17.0426 4.84012 17.1311 4.39879 16.7991L1.20651 14.3973C-0.388615 13.1971 -0.388621 10.8029 1.2065 9.60276L4.39879 7.20093C4.84012 6.86889 5.46705 6.95747 5.7991 7.39879Z" fill="#3d5690"></path> <path d="M18.2009 16.6012C17.8689 16.1599 17.9575 15.533 18.3988 15.2009L21.5911 12.7991C22.1228 12.399 22.1228 11.601 21.5911 11.2009L18.3988 8.7991C17.9575 8.46705 17.8689 7.84012 18.2009 7.39879C18.533 6.95747 19.1599 6.86889 19.6012 7.20093L22.7935 9.60276C24.3886 10.8029 24.3886 13.1971 22.7935 14.3973L19.6012 16.7991C19.1599 17.1311 18.533 17.0426 18.2009 16.6012Z" fill="#3d5690"></path> </g></svg>
         </div>
         <h6 class="text-xs font-medium text-indigo-900 mt-1">Skills</h6>
       </div>
       
       </button>
     </RouterLink>

    <!-- Button 3 -->
     <RouterLink to="/projects">
       <button
         class=" mx-2
                transition-transform duration-200 ease-in-out
                hover:scale-110 cursor-pointer"
       >
       
       <div>
         <div class="flex items-center justify-center">
           <svg class="w-4 h-4" fill="#3d5690" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg"><g id="SVGRepo_bgCarrier" stroke-width="0"></g><g id="SVGRepo_tracerCarrier" stroke-linecap="round" stroke-linejoin="round"></g><g id="SVGRepo_iconCarrier"> <path fill-rule="evenodd" d="M16,16 L16,13 L18,13 L18,16 L21,16 L21,18 L18,18 L18,21 L16,21 L16,18 L13,18 L13,16 L16,16 Z M4,13 L9,13 C10.1045695,13 11,13.8954305 11,15 L11,20 C11,21.1045695 10.1045695,22 9,22 L4,22 C2.8954305,22 2,21.1045695 2,20 L2,15 C2,13.8954305 2.8954305,13 4,13 Z M4,15 L4,20 L9,20 L9,15 L4,15 Z M4,2 L9,2 C10.1045695,2 11,2.8954305 11,4 L11,9 C11,10.1045695 10.1045695,11 9,11 L4,11 C2.8954305,11 2,10.1045695 2,9 L2,4 C2,2.8954305 2.8954305,2 4,2 Z M4,4 L4,9 L9,9 L9,4 L4,4 Z M15,2 L20,2 C21.1045695,2 22,2.8954305 22,4 L22,9 C22,10.1045695 21.1045695,11 20,11 L15,11 C13.8954305,11 13,10.1045695 13,9 L13,4 C13,2.8954305 13.8954305,2 15,2 Z M15,4 L15,9 L20,9 L20,4 L15,4 Z"></path> </g></svg>
         </div>
         <h6 class="text-xs font-medium text-indigo-900 mt-1">Projects</h6>
       </div>
       
       </button>
     </RouterLink>

    <!-- Button 4 -->
     <RouterLink to="/contact-me">
       <button
         class=" mx-2
                transition-transform duration-200 ease-in-out
                hover:scale-110 cursor-pointer"
       >
       
       <div>
         <div class="flex items-center justify-center">
           <svg class="w-4 h-4" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg"><g id="SVGRepo_bgCarrier" stroke-width="0"></g><g id="SVGRepo_tracerCarrier" stroke-linecap="round" stroke-linejoin="round"></g><g id="SVGRepo_iconCarrier"> <path opacity="0.5" d="M14.5562 15.5477L14.1007 16.0272C14.1007 16.0272 13.0181 17.167 10.0631 14.0559C7.10812 10.9448 8.1907 9.80507 8.1907 9.80507L8.47752 9.50311C9.18407 8.75924 9.25068 7.56497 8.63424 6.6931L7.37326 4.90961C6.61028 3.8305 5.13596 3.68795 4.26145 4.60864L2.69185 6.26114C2.25823 6.71766 1.96765 7.30945 2.00289 7.96594C2.09304 9.64546 2.81071 13.259 6.81536 17.4752C11.0621 21.9462 15.0468 22.1239 16.6763 21.9631C17.1917 21.9122 17.6399 21.6343 18.0011 21.254L19.4217 19.7584C20.3806 18.7489 20.1102 17.0182 18.8833 16.312L16.9728 15.2123C16.1672 14.7486 15.1858 14.8848 14.5562 15.5477Z" fill="#3d5690"></path> <path d="M17 12C19.7614 12 22 9.76142 22 7C22 4.23858 19.7614 2 17 2C14.2386 2 12 4.23858 12 7C12 7.79984 12.1878 8.55582 12.5217 9.22624C12.6105 9.4044 12.64 9.60803 12.5886 9.80031L12.2908 10.9133C12.1615 11.3965 12.6035 11.8385 13.0867 11.7092L14.1997 11.4114C14.392 11.36 14.5956 11.3895 14.7738 11.4783C15.4442 11.8122 16.2002 12 17 12Z" fill="#3d5690"></path> </g></svg>
         </div>
         <h6 class="text-xs font-medium text-indigo-900 mt-1">Contact</h6>
       </div>
       
       </button>
     </RouterLink>

    <!-- Button 5 -->
  </div>
</template>

<style scoped>
  /* Animación */
@keyframes float {
  0% {
    transform: translateY(0);
  }

  50% {
    transform: translateY(-10px);
  }

  100% {
    transform: translateY(0);
  }
}

.float-animation {
  animation: float 2s ease-in-out infinite;
}

</style>

