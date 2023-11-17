<template>
  <div class="mt-4">
    <label for="softwareSelect" class="block text-sm font-medium text-gray-700"
      >Select Accounting Software</label
    >
    <select
      id="softwareSelect"
      v-model="selectedSoftware"
      class="mt-1 block w-full pl-3 pr-10 py-2 text-base border-gray-300 focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 sm:text-sm rounded-md"
    >
      <option disabled value="">Choose software...</option>
      <option
        v-for="software in softwareOptions"
        :key="software"
        :value="software"
      >
        {{ software }}
      </option>
    </select>
  </div>
</template>

<script setup>
import { ref } from "vue";

const softwareOptions = ["Xero", "MYOB", "QuickBooks"];
const selectedSoftware = ref("");
</script>
