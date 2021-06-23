<template>
  <div id="rectangle">
    <p>J’accepte de partager mes données avec l’équipe Detectoux</p>
    <router-link to="/Contribue1">
      <button></button>
    </router-link>
  </div>
</template>

<script>
</script>

<style scoped>
#rectangle {
  position: absolute;
  width: 50%;
  height: 30%;
  margin-left: 25%;
  box-shadow: 6px 8px 8px #2e3244;
  background: #f1895c;
  display: flex;
  top: 30%;
}
button {
  width: 21px;
  height: 21px;
  background: #ffffff;
  margin-left: 45%;
  top: 75%;
  transform: translateY(-50%);
}
p {
  font-family: "Lucida Sans", "Lucida Sans Regular", "Lucida Grande",
    "Lucida Sans Unicode", Geneva, Verdana, sans-serif;
  font-style: normal;
  font-weight: normal;
  float: left;
  display: flex;
  color: #2e3244;
  text-align: center;
  margin: auto;
  align-items: center;
  justify-content: center;
}
</style>