/// <reference types="vite/client" />Copyright (c) 2025 Author. All Rights Reserved.
/// <reference types="vite/client" />

declare module '*.vue' {
  import type { DefineComponent } from 'vue'
  const component: DefineComponent<{}, {}, any>
  export default component
}

