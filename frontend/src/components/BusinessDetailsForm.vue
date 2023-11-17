<template>
  <form @submit.prevent="submitForm" class="space-y-4">
    <div>
      <label for="businessName" class="block text-sm font-medium text-gray-700">
        Business Name
      </label>
      <input
        id="businessName"
        v-model="businessName"
        type="text"
        class="mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-indigo-300 focus:ring focus:ring-indigo-200 focus:ring-opacity-50"
        placeholder="Enter business name"
        required
      />
    </div>

    <div>
      <label
        for="yearEstablished"
        class="block text-sm font-medium text-gray-700"
      >
        Year Established
      </label>
      <input
        id="yearEstablished"
        v-model.number="yearEstablished"
        type="number"
        class="mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-indigo-300 focus:ring focus:ring-indigo-200 focus:ring-opacity-50"
        placeholder="Enter establishment year"
        required
      />
    </div>

    <button
      type="submit"
      class="px-4 py-2 bg-indigo-600 hover:bg-indigo-700 text-white font-bold rounded-md"
    >
      Submit
    </button>
  </form>
</template>

<script setup>
import { ref } from "vue";
import { submitLoanApplication } from "../services/apiService";

const businessName = ref("");
const yearEstablished = ref("");
const balanceSheet = ref([
  {
    year: 2020,
    month: 12,
    profitOrLoss: 250000,
    assetsValue: 1234,
  },
  {
    year: 2020,
    month: 11,
    profitOrLoss: 1150,
    assetsValue: 5789,
  },
  {
    year: 2020,
    month: 10,
    profitOrLoss: 2500,
    assetsValue: 22345,
  },
  {
    year: 2020,
    month: 9,
    profitOrLoss: -187000,
    assetsValue: 223452,
  },
]);
const submitForm = async () => {
  const applicationData = {
    businessName: businessName.value,
    yearEstablished: yearEstablished.value,
    balanceSheet: balanceSheet.value,
  };

  try {
    const response = await submitLoanApplication(applicationData);
    console.log("Response from server:", response);
  } catch (error) {
    console.error("Error submitting application:", error);
  }
};
</script>
