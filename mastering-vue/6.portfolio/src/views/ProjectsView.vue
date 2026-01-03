<script setup>
    import Heading from '@/components/Heading.vue';
    import Subheading from '@/components/Subheading.vue';
    import ProjectCard from '@/components/ProjectCard.vue';
    import { onMounted, nextTick } from 'vue'
    import AOS from 'aos'
    import 'aos/dist/aos.css'

    onMounted(async () => {
        await nextTick()
        AOS.init()
        AOS.refresh()
    })

    import Stejos from '@/assets/projects/hero-stejos.webp'
    import Jepaks from '@/assets/projects/jepaks-hero.webp'
    import Academy from '@/assets/projects/academy-hero.webp'
    import Events from '@/assets/projects/events-hero.webp'
    import Nsm from '@/assets/projects/Nairobi-Spaces-mobile.webp'
    import Nsd from '@/assets/projects/Nairobi-Spaces-desktop.webp'
    import Explore from '@/assets/projects/explore-hero.webp'

    const projectsList = [
      {
        "id": 1,
        "link": "https://www.stejostours.com/",
        "image": Jepaks,
        "industry": "IT & Software",
        "date": "3rd October, 2025",
        "projectname": "Jepaks Systems",
        "tech": [
          "NextJS",
          "TypeScript",
          "TailwindCSS",
          "MongoDB",
          "ExpressJS",
        ]
      },
      {
        "id": 2,
        "link": "https://academy.jepaks.com/",
        "image": Academy,
        "industry": "EdTech",
        "date": "3rd Decmber, 2025",
        "projectname": "Jepaks Academy",
        "tech": [
          "NextJS",
          "TypeScript",
          "TailwindCSS",
          "MongoDB",
          "ExpressJS",
        ]
      },
      {
        "id": 3,
        "link": "https://www.stejostours.com/",
        "image": Stejos,
        "industry": "Tourism",
        "date": "1st January, 2026",
        "projectname": "Stejos Tours & Travel",
        "tech": [
          "Django",
          "AlpineJS",
          "HTMX",
          "TailwindCSS",
          "PostrgreSQL"
        ]
      },
      {
        "id": 4,
        "link": "https://www.eventsparlour.com/",
        "image": Events,
        "industry": "Events & Entertainment",
        "date": "COMING SOON",
        "projectname": "Events Parlour",
        "tech": [
          "NextJS",
          "TypeScript",
          "TailwindCSS",
          "PostrgreSQL"
        ]
      },
      {
        "id": 5,
        "link": "#",
        "image": Explore,
        "industry": "Tourism & AirBnB",
        "date": "COMING SOON",
        "projectname": "Explore Masters Tours & Travel",
        "tech": [
          "Django",
          "AlpineJS",
          "HTMX",
          "TailwindCSS",
          "PostrgreSQL"
        ]
      },
      {
        "id": 6,
        "link": "https://www.figma.com/proto/fszR7UEd43gr1wtXxnCBQv/NAIROBI-SPACES?node-id=167-1620&p=f&t=sIbmlpWmL4NDkr0u-0&scaling=min-zoom&content-scaling=fixed&page-id=143%3A558&starting-point-node-id=167%3A1620",
        "image": Nsm,
        "industry": "AirBnB",
        "date": "5th June 2025",
        "projectname": "Nairobi Spaces | UI/UX Design | Mobile Screen",
        "tech": [
          "Figma",
        ]
      },
      {
        "id": 7,
        "link": "https://www.figma.com/proto/fszR7UEd43gr1wtXxnCBQv/NAIROBI-SPACES?node-id=148-1103&t=95ordY6dKRRbhsbr-0&scaling=min-zoom&content-scaling=fixed&page-id=143%3A557&starting-point-node-id=148%3A1103",
        "image": Nsd,
        "industry": "AirBnB",
        "date": "5th June 2025",
        "projectname": "Nairobi Spaces | UI/UX Design | Desktop Screen",
        "tech": [
          "Figma",
        ]
      },

    ]
</script>

<template>
<section class="min-h-screen flex items-center" data-aos="fade-up" data-aos-duration="1000">
    <div class="my-10">
      <div class="p-3 mb-10">
          <Heading label="Projects/Tools I've built..."/>
          <p>
            Where I actively participated, collaborated and engineered greatness
          </p>
      </div>
      <div class="grid grid-cols-1 sm:grid-cols-1 md:grid-cols-3 lg:grid-cols-4 items-center gap-x-20 gap-y-10">
        <ProjectCard 
          v-for="project in projectsList" 
          :key="project.id"
          :link="project.link"
          :image="project.image"
          :industry="project.industry"
          :date="project.date"
          :projectname="project.projectname"
          :tech="project.tech"
        />
      </div>
    </div>
</section>
<section class="mb-30">
  <Heading label="More to come..." class="text-center"/>
  
</section>

</template>

<style scoped>

</style>