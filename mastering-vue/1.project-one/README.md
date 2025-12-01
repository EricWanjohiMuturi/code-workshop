# What will you learn?
1. Creating a Vue application
2. Displaying data using interpolation
3. Basic reactivity with ref()
4. Computed values with computed()
5. Conditional CSS classes
6. Binding form inputs to refs

## Installing Vue
- Install Vue using CDN -> <script src="https://unpkg.com/vue@3/dist/vue.global.js"></script>
- Focus is on the Composition API and not Methods. 

## Reactivity
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