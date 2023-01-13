import { createApp } from 'vue'
import App from "./App.vue"
import Item from "./components/Item.vue"
import './style.css'
const app = createApp(App)

app.component("item", Item);

app.mount('#app')
