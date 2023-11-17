<template>
  <div id="app" class="p-4">
    <BusinessDetailsForm />
    <AccountingSoftwareSelector />
    <BalanceSheetDisplay />
  </div>
</template>

<script>
import BusinessDetailsForm from "./components/BusinessDetailsForm.vue";
import AccountingSoftwareSelector from "./components/AccountingSoftwareSelector.vue";
import BalanceSheetDisplay from "./components/BalanceSheetDisplay.vue";

export default {
  name: "App",
  components: {
    BusinessDetailsForm,
    AccountingSoftwareSelector,
    BalanceSheetDisplay,
  },
};
</script>
