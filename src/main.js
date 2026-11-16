import { mount } from 'svelte'
import './app.css'
import App from './App.svelte'

const target = document.getElementById('app')

if (!target) {
  throw new Error('No se encontró el elemento raíz de la aplicación (#app).')
}

target.replaceChildren()

export default mount(App, { target })
