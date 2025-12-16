 <template>
    <div class="relative">
    <button
        class="text-red-500 hover:text-red-600 mx-2
                transition-transform duration-200 ease-in-out
                hover:scale-110 focus:outline-none
                focus:ring-2 focus:ring-red-500 rounded-full"
        @click="toggleDropdown"
    >
        <div>
        <div class="flex items-center justify-center">
            <svg class="w-4 h-4" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg"><g id="SVGRepo_bgCarrier" stroke-width="0"></g><g id="SVGRepo_tracerCarrier" stroke-linecap="round" stroke-linejoin="round"></g><g id="SVGRepo_iconCarrier"> <path d="M4 12H20M12 4V20" stroke="#3d5690" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"></path> </g></svg>
        </div>
        <h6 class="text-xs text-indigo-900 mt-1">More</h6>
        </div>
    </button>

    <div v-if="isDropdownOpen" class="absolute bg-white shadow-lg rounded mt-2">
        <ul>
        <li class="px-4 py-2 hover:bg-gray-100 cursor-pointer">Menu Item 1</li>
        <li class="px-4 py-2 hover:bg-gray-100 cursor-pointer">Menu Item 2</li>
        <li class="px-4 py-2 hover:bg-gray-100 cursor-pointer">Menu Item 3</li>
        </ul>
    </div>
    </div>
</template>

<script setup>
import { ref, onMounted, onUnmounted } from 'vue'

const isHidden = ref(false)
const isDropdownOpen = ref(false)
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

const toggleDropdown = () => {
    isDropdownOpen.value = !isDropdownOpen.value
}

const closeDropdown = (event) => {
    if (!event.target.closest('.relative')) {
    isDropdownOpen.value = false
    }
}

onMounted(() => {
    window.addEventListener('scroll', handleScroll, { passive: true })
    window.addEventListener('click', closeDropdown)
})

onUnmounted(() => {
    window.removeEventListener('scroll', handleScroll)
    window.removeEventListener('click', closeDropdown)
})
</script>