<template>
  <div id="app">
    <Header />
    <Test3_1 />
    <Footer />
  </div>
</template>

<script>
import Header from "./components/Header.vue";
import Footer from "./components/Footer.vue";
import Test3_1 from "./views/Test3_1.vue";

export default {
  name: "App",
  components: {
    Header,
    Footer,
    Test3_1,
  },
};
</script>

<style>
body {
  background-color: #516079;
}
#app {
  font-family: "Lucida Sans", "Lucida Sans Regular", "Lucida Grande",
    "Lucida Sans Unicode", Geneva, Verdana, sans-serif;
  text-align: center;
  color: #2e3244;
}
</style>
