<script setup>
import { ref } from "vue";
import { submitLoanApplication } from "../services/apiService";
import AccountingSoftwareSelector from "../components/AccountingSoftwareSelector.vue";
import BalanceSheetDisplay from "../components/BalanceSheetDisplay.vue";
const businessName = ref("");
const yearEstablished = ref("");
const isLoading = ref(false);
const errorMessage = ref("");
const preAssessment = ref(null);
const currentYear = new Date().getFullYear();
const minYear = 1900;
const balanceSheet = [
  {
    year: 2020,
    month: 12,
    profitOrLoss: -250000,
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
];
const submitForm = async () => {
  isLoading.value = true;
  errorMessage.value = "";
  preAssessment.value = null;

  const applicationData = {
    businessName: businessName.value,
    yearEstablished: yearEstablished.value,
    balanceSheet: balanceSheet,
  };

  try {
    const response = await submitLoanApplication(applicationData);

    if (Object.prototype.hasOwnProperty.call(response, "pre_assessment")) {
      preAssessment.value = response.pre_assessment;
    } else {
      preAssessment.value = 0;
      console.warn("Pre-assessment data missing in the response");
    }
  } catch (error) {
    errorMessage.value = "Failed to submit application.";
    console.error("Error submitting application:", error);
  } finally {
    isLoading.value = false;
  }
};
</script>
<template>
  <div class="flex justify-center items-center min-h-screen bg-gray-100">
    <div
      class="w-full max-w-lg p-6 bg-white rounded-lg border shadow-md sm:p-8 lg:p-10"
    >
      <div v-if="errorMessage" class="text-red-700">
        <p>
          <strong>Pre-Assessment Value: </strong>
          <strong>{{ errorMessage }}</strong>
        </p>
      </div>
      <div v-if="preAssessment" class="text-green-700">
        <p>
          <strong>Pre-Assessment Value:</strong>
          <strong>{{ preAssessment }}</strong>
        </p>
      </div>
      <form @submit.prevent="submitForm" class="space-y-4">
        <div>
          <label
            for="businessName"
            class="block text-sm font-medium text-gray-700"
          >
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
            :min="minYear"
            :max="currentYear"
            required
          />
        </div>
        <AccountingSoftwareSelector />
        <BalanceSheetDisplay :balanceSheet="balanceSheet" />
        <button
          type="submit"
          class="w-full px-5 py-3 text-sm font-medium text-white bg-indigo-600 hover:bg-indigo-700 rounded-lg"
        >
          Submit
        </button>
      </form>
    </div>
  </div>
</template>
