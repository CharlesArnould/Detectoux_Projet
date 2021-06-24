<template>
  <div class="test1">
    <div class="test1_étape1">
      <p><b>Etape 1</b></p>
    </div>
    <div class="test1_wrapper">
      <div class="test1_wrapper_rectangle">
        <div class="test1_wrapper_rectangle_form">
          <div class="test1_wrapper_rectangle_form_texte">
            <p>
              Pour commencer, veuillez renseigner quelques informations à votre
              sujet :
            </p>
          </div>
          <div class="test1_wrapper_rectangle_form_ddn">
            <label for="ddn">Date de naissance :&nbsp;</label>
            <input type="date" id="ddn" required />
          </div>
          <br />
          <div class="test1_wrapper_rectangle_form_sexe">
            <label for="sexe">Sexe :&nbsp;</label>
            <select id="sexe" required>
              <option value="">Choix</option>
              <option value="femme">Femme</option>
              <option value="homme">Homme</option>
            </select>
          </div>
          <br />
          <div class="test1_wrapper_rectangle_form_button">
            <router-link to="/Play">
              <button>
                <b>Etape suivante</b>
              </button>
            </router-link>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
</script>

<style scoped>
.test1 {
  display: flex;
  justify-content: center;
  align-items: center;
  height: 80vh;
  width: 100vw;
  flex-direction: column;
}

.test1_étape1 {
  width: 25vw;
  height: 7vh;
  background: #f1895c;
  box-shadow: 6px 8px 8px #2e3244;
  font-weight: bold;
  display: flex;
  flex-direction: column;
  margin: 20px;
}

.test1_wrapper {
  display: flex;
  justify-content: center;
  align-items: center;
  height: 50vh;
  width: 90vw;
  margin: 80px;
}

.test1_wrapper_rectangle {
  box-shadow: 6px 8px 8px #2e3244;
  background: #c4c4c4;
  display: flex;
  justify-content: center;
  align-items: center;
  padding: 60px;
}

.test1_wrapper_rectangle_form {
  display: flex;
  align-items: center;
  flex-direction: column;
}

.test1_wrapper_rectangle_form_texte {
  display: flex;
  justify-content: center;
  align-items: center;
}

.test1_wrapper_rectangle_form_ddn {
  display: flex;
  justify-content: center;
  align-items: center;
}

button {
  background: #f1895c;
  margin: 5px;
  height: 6vh;
  width: 50vw;
  font-family: "Lucida Sans", "Lucida Sans Regular", "Lucida Grande",
    "Lucida Sans Unicode", Geneva, Verdana, sans-serif;
  color: #2e3244;
}

p {
  font-family: "Lucida Sans", "Lucida Sans Regular", "Lucida Grande",
    "Lucida Sans Unicode", Geneva, Verdana, sans-serif;
  font-style: normal;
  font-weight: normal;
  float: left;
  color: #2e3244;
  text-align: center;
  align-items: center;
  justify-content: center;
}
</style>