<template>
  <div id="app">
    <NavigationBar />
    <router-view />
    <MainFooter />
  </div>
</template>

<script>
import NavigationBar from "./components/NavigationBar.vue";
import MainFooter from "./components/MainFooter.vue";

export default {
  components: {
    NavigationBar,
    MainFooter,
  },
};
</script>
<style></style>
