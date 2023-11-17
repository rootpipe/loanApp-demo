<script setup>
import { defineProps } from "vue";

const props = defineProps({
  balanceSheet: {
    type: Array,
    required: true,
  },
});

const formatCurrency = (value) => {
  return "$" + value.toFixed(2);
};
const getClassForProfitOrLoss = (profitOrLoss) => {
  return {
    "px-2 inline-flex text-xs leading-5 font-semibold rounded-full": true,
    "bg-green-100 text-green-800": profitOrLoss > 0,
    "bg-red-100 text-red-800": profitOrLoss <= 0,
  };
};
</script>
<template>
  <div class="mt-6">
    <h3 class="text-lg leading-6 font-medium text-gray-900">Balance Sheet</h3>
    <ul
      class="mt-2 max-w-xl bg-white rounded-md shadow overflow-hidden divide-y divide-gray-200"
    >
      <li
        v-for="(item, index) in props.balanceSheet"
        :key="index"
        class="px-4 py-4 sm:px-6"
      >
        <div class="flex items-center justify-between">
          <p class="text-sm font-medium text-indigo-600 truncate">
            {{ item.month }}/{{ item.year }}
          </p>
          <div class="ml-2 flex-shrink-0 flex">
            <p :class="getClassForProfitOrLoss(item.profitOrLoss)">
              {{ item.profitOrLoss > 0 ? "Profit" : "Loss" }}
            </p>
          </div>
        </div>
        <div class="mt-2 sm:flex sm:justify-between">
          <div class="sm:flex">
            <p class="flex items-center text-sm text-gray-500">
              Profit/Loss: {{ formatCurrency(item.profitOrLoss) }}
            </p>
            <p
              class="mt-2 flex items-center text-sm text-gray-500 sm:mt-0 sm:ml-6"
            >
              Assets: {{ formatCurrency(item.assetsValue) }}
            </p>
          </div>
        </div>
      </li>
    </ul>
  </div>
</template>
