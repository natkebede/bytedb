<script setup lang="ts">
const workspaceStore = useWorkspace()

const { navigateToFeed } = workspaceStore

const { isFeedPageOpened } = storeToRefs(workspaceStore)

const { isNewFeedAvailable } = useProductFeed()

const gotoFeed = () => navigateToFeed()
const router = useRouter()
const route = useRoute()

// Functions to navigate to each page
const gotoWorkflow = () => {
  router.push('/workflow')
}
const gotoWorkspace = () => {
  router.push('/workspace')
}
const gotoReporting = () => {
  router.push('/reporting')
}

// Computed properties to check active page
const isWorkflowPageOpened = computed(() => route.path === '/workflow')
const isWorkspacePageOpened = computed(() => route.path === '/workspace')
const isReportingPageOpened = computed(() => route.path === '/reporting')
</script>

<template>
  <!-- Workflow Button -->
  <NcButton type="text" full-width size="xsmall" class="my-0.5 w-full !h-7 !rounded-md !font-normal !pl-4.5 !pr-5"
    :centered="false" :class="{
      '!text-brand-600 !bg-brand-50 !hover:bg-brand-50': isWorkflowPageOpened,
      '!hover:(bg-gray-200 text-gray-700)': !isWorkflowPageOpened,
    }" @click="gotoWorkflow">
    <div class="flex !w-full items-center gap-2" :class="{ 'font-semibold': isWorkflowPageOpened }">
      <span>Workflow</span>
    </div>
  </NcButton>

  <!-- Workspace Button -->
  <NcButton type="text" full-width size="xsmall" class="my-0.5 w-full !h-7 !rounded-md !font-normal !pl-4.5 !pr-5"
    :centered="false" :class="{
      '!text-brand-600 !bg-brand-50 !hover:bg-brand-50': isWorkspacePageOpened,
      '!hover:(bg-gray-200 text-gray-700)': !isWorkspacePageOpened,
    }" @click="gotoWorkspace">
    <div class="flex !w-full items-center gap-2" :class="{ 'font-semibold': isWorkspacePageOpened }">
      <span>Workspace</span>
    </div>
  </NcButton>


  <!-- Reporting Button -->
  <NcButton type="text" full-width size="xsmall" class="my-0.5 w-full !h-7 !rounded-md !font-normal !pl-4.5 !pr-5"
    :centered="false" :class="{
      '!text-brand-600 !bg-brand-50 !hover:bg-brand-50': isReportingPageOpened,
      '!hover:(bg-gray-200 text-gray-700)': !isReportingPageOpened,
    }" @click="gotoReporting">
    <div class="flex !w-full items-center gap-2" :class="{ 'font-semibold': isReportingPageOpened }">
      <span>Reporting</span>
    </div>
  </NcButton>
</template>

<style scoped lang="scss">
@keyframes pulse {
  0% {
    transform: scale(1);
    opacity: 1;
  }

  50% {
    transform: scale(1.1);
    opacity: 0.7;
  }

  100% {
    transform: scale(1);
    opacity: 1;
  }
}

.pulsing-dot {
  animation: pulse 1.5s infinite ease-in-out;
}

:deep(.nc-btn-inner) {
  @apply !w-full;
}
</style>