<template>
  <div id="app">
    <Header />
    <Home />
    <Footer />
  </div>
</template>

<script>
import Header from "./components/Header.vue";
import Footer from "./components/Footer.vue";
import Home from "./views/Home.vue";

export default {
  name: "App",
  components: {
    Header,
    Footer,
    Home,
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
