<template>
  <div>
    <div class="rectangle">
      <p>
        Bienvenue sur<b> Detectoux</b> ! <br /><br />
        En quelques étapes, obtenez un diagnostic rapide sur la présence de la<b>
          Covid-19</b
        >.<br /><br />
        Si vous possédez un test Covid-19, qu’il soit positif ou négatif, vous
        pouvez nous aider à améliorer le diagnostic en contribuant à notre base
        de données.
      </p>
    </div>
    <div class="choix">
      <button><b>Je me teste</b></button>
      <button><b>Je contribue</b></button>
    </div>
  </div>
</template>

<script>
export default {
  name: "Home",
  props: {
    msg: String,
  },
};
</script>

<style scoped>
.rectangle {
  position: absolute;
  width: 90%;
  height: 40%;
  margin-left: 5%;
  box-shadow: 6px 8px 8px #2e3244;
  background: #c4c4c4;
  display: flex;
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
button {
  box-shadow: 6px 8px 8px #2e3244;
  background: #f1895c;
}
.choix {
  margin-left: 5%;
}
</style>