<template>
  <div id="app" class="p-4">
    <BusinessDetailsForm />
  </div>
</template>

<script>
import BusinessDetailsForm from "./components/BusinessDetailsForm.vue";
export default {
  name: "App",
  components: {
    BusinessDetailsForm,
  },
};
</script>
