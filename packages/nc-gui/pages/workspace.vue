<!-- pages/workspace.vue -->
<template>
  <div class="iframe-container">
    <iframe
      :src="iframeSrc"
      frameborder="0"
      style="width: 100%; height: 100vh;"
      allowfullscreen
    ></iframe>
  </div>
</template>

<script setup lang="ts">
// Define the source URL for the iframe
const iframeSrc = 'http://localhost:8888/lab?' // Replace with your URL
</script>

<style scoped>
.iframe-container {
  width: 100%;
  height: 100vh; /* Adjust as needed */
}
</style>