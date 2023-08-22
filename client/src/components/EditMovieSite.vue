<template>
  <div class="modal">
    <div class="modal-content">
      <h2 v-if="isEditMode">Edit Movie Site</h2>
      <h2 v-else>Create Movie Site</h2>

      <form @submit.prevent="saveSite">
        <label for="siteName">Site Name</label>
        <input v-model="formData.site_name" id="siteName" />

        <label for="province">Province</label>
        <input v-model="formData.province" id="province" />

        <label for="city">City</label>
        <input v-model="formData.city" id="city" />

        <!-- Other form fields -->

        <button type="submit">{{ isEditMode ? 'Save' : 'Create' }}</button>
      </form>
    </div>
  </div>
</template>

<script>
export default {
  props: ['site'],
  data() {
    return {
      isEditMode: false,
      formData: {
        site_name: '',
        province: '',
        city: '',
        // Other form data
      },
    };
  },
  watch: {
    site: {
      immediate: true,
      handler(newSite) {
        if (newSite) {
          this.isEditMode = true;
          this.formData = { ...newSite };
        }
      },
    },
  },
  methods: {
    saveSite() {
      if (this.isEditMode) {
        // Perform API request to update the site
      } else {
        // Perform API request to create a new site
      }
      this.$emit('saved');
    },
  },
};
</script>

<style scoped>
/* Styles for the modal */
</style>
