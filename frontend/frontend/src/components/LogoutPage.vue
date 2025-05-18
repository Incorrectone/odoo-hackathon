<template>
  <div class="container">
    <div class="container py-3"></div>
    Logging you out...
  </div>
</template>

<script>
export default {
  name: "LogoutPage",
  data() {},
  created() {
    this.logout();
  },
  methods: {
    logout() {
      if (localStorage.getItem("token")) {
        localStorage.removeItem("token");
        localStorage.removeItem("role");
        localStorage.removeItem("userid");
        window.location.reload();
      }
      location.replace("/");
    },
  },
};
</script>
