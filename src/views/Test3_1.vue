<template>
  <div class="test">
    <div class="test_resultats">
      <p><b>Résultats</b></p>
    </div>
    <div class="test_wrapper">
      <div class="test_wrapper_analyse">
        <p>
          Après analyse de votre toux, nous avons détécté une possible présence
          de la Covid-19 à hauteur de :
        </p>
        <div class="test_wrapper_pourcentage">
          <!-- Afficher le pourcentage -->
          <p><b>4%</b></p>
        </div>
      </div>
    </div>
    <div class="test_message">
      <p>
        Nous rappelons qu’il est important de continuer à
        <b> &nbsp;respecter les gestes barrières&nbsp; </b>
        !
      </p>
    </div>
  </div>
</template>

<script>
</script>

<style scoped>
.test {
  display: flex;
  justify-content: center;
  align-items: center;
  height: 90vh;
  width: 100vw;
  flex-direction: column;
}

.test_resultats {
  width: 25vw;
  height: 7vh;
  background: #f1895c;
  box-shadow: 6px 8px 8px #2e3244;
  font-weight: bold;
  display: flex;
  flex-direction: column;
  /* margin */
}

.test_wrapper_analyse {
  width: 90vw;
  height: 30vh;
  background: #c4c4c4;
  box-shadow: 6px 8px 8px #2e3244;
  display: flex;
  flex-direction: column;
}

.test_wrapper_pourcentage {
  font-weight: bold;
}

.test_message {
  width: 90%;
  height: 25%;
  background: #c4c4c4;
  box-shadow: 6px 8px 8px #2e3244;
  display: flex;
  justify-content: center;
  align-items: center;
  flex-direction: column;

  border-color: #f1895c;
  border-style: solid;
}

p {
  font-family: "Lucida Sans", "Lucida Sans Regular", "Lucida Grande",
    "Lucida Sans Unicode", Geneva, Verdana, sans-serif;
  font-style: normal;
  text-align: center;
  color: #2e3244;
  font-weight: normal;
  margin: auto;
  align-items: center;
  justify-content: center;
}
</style>