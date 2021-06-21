<template>
  <div class="rectangle">
    <p>Nous vous remercions de votre contribution !</p>
  </div>
</template>

<script>
export default {
  name: "remerciements",
  props: {
    msg: String,
  },
};
</script>

<style scoped>
.rectangle {
  position: absolute;
  width: 1231px;
  height: 221px;
  left: 98px;
  box-shadow: 0px 2px 3px #2e3244;
  background: #c4c4c4;
}
p {
  font-family: Raleway;
  font-style: normal;
  font-size: 24px;
  line-height: 28px;
  text-align: center;
  color: #2e3244;
}
</style>