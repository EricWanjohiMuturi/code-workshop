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

## Single File Components (SFC)
Vue Single File Components are `.vue` files that encapsulate a component's template, script, and styles in one file:

```vue
<template>
    <div class="counter">
        <p>Count: {{ count }}</p>
        <button @click="count++">Increment</button>
    </div>
</template>

<script setup>
import { ref } from 'vue'

const count = ref(0)
</script>

<style scoped>
.counter {
    padding: 1rem;
    border: 1px solid #ccc;
}
</style>
```

Each section (`<template>`, `<script>`, `<style>`) handles a specific concern, making components modular and maintainable.

## Separation of Concerns in Vue
Vue embraces separation of concerns by organizing code into distinct layers:

- **Template** - Declarative markup for the UI structure
- **Script** - Business logic, state management, and methods
- **Styles** - Component-specific styling with `scoped` attribute to prevent style leakage

This approach differs from traditional web development where HTML, CSS, and JavaScript were kept separate across different files. Vue's SFC model keeps related code together while maintaining clear boundaries, improving readability and maintainability.
```
"Seperation Of Concerns is not equal to the seperation of file types, rather it is the separation by purpose through components"
```
## Key Concepts to note:
- **Single File Components (SFC)** - Structuring Vue components with template, script, and styles in `.vue` files
- **Component-Based Architecture** - Building modular, reusable UI pieces by purpose
- **Reactivity Basics** - Using `ref()` to create reactive state that automatically updates the UI
- **Text Interpolation** - Displaying dynamic data in templates using the `{{ }}` syntax
- **Attribute Binding** - Using `v-bind:` or `:` to dynamically bind HTML attributes to reactive data
- **Event Handling** - Using `@` to listen to DOM events with optional modifiers like `@click.prevent` or `@submit.stop`
- **Conditional Rendering** - Using `v-if`, `v-else-if`, `v-else`, and `v-show` to display or hide elements based on conditions
- **List Rendering** - Using `v-for` to render lists of items from arrays or objects with unique key binding