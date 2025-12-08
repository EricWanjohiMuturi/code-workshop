# What will you learn?
1. Creating a Vue application
2. Displaying data using interpolation
3. Basic reactivity with ref()
4. Computed values with computed()
5. Conditional CSS classes
6. Binding form inputs to refs


## Vue - What & Why?
Vue is a progressive JavaScript framework for building user interfaces with reactive data binding and component-based architecture. It allows developers to create dynamic, interactive web applications with less boilerplate code.

## Using the Vue CDN
You can quickly get started with Vue by including it via CDN:
```html
<script src="https://unpkg.com/vue@3/dist/vue.global.js"></script>
```
This approach is ideal for adding Vue to existing projects or learning without build tools.

- Focus is on the Composition API and not Methods API style of authoring Vue applications. 

## Reactivity in Vue
- In composition API, the recommended way to declare reactive state is using the ref() function

```text
import { ref } from 'vue'

const count = ref(0)
```

ref() takes the argument and returns it wrapped within a ref object with a ```.value``` property:

```text
const count = ref(0)

console.log(count) // { value: 0 }
console.log(count.value) // 0

count.value++
console.log(count.value) // 1

```

## Installing Vue Locally using create-vue
For larger projects, install Vue locally using the official scaffolding tool:
```bash
npm create vue@latest
```
Follow the prompts to configure your project with TypeScript, Router, Pinia, and other tools as needed.

## The Vue Project Anatomy
A typical Vue project structure includes:
- `src/` - Source files (components, assets, main.js)
- `src/components/` - Reusable Vue components
- `src/App.vue` - Root component
- `src/main.js` - Application entry point
- `package.json` - Project dependencies and scripts
- `vite.config.js` - Build configuration (when using Vite)
- `public/` - Static assets