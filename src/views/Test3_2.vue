<template>
  <div>
    <div id="resultats">
      <p>Résultats</p>
    </div>
    <div id="analyse">
      <p>
        Après analyse de votre toux, nous avons détécté une possible présence de
        la Covid-19 à hauteur de :
      </p>
      <!-- Afficher le pourcentage -->
    </div>
    <div id="message">
      <p>
        Merci de contacter votre médecin au plus vite et de
        <strong>&nbsp;respecter les gestes barrières</strong>
        &nbsp;afin de protéger vos proches.
      </p>
    </div>
  </div>
</template>

<script>
</script>

<style scoped>
#resultats {
  position: absolute;
  width: 25%;
  height: 7%;
  left: 40%;
  top: 10%;
  background: #f1895c;
  box-shadow: 6px 8px 8px #2e3244;
  font-weight: bold;
  display: flex;
  flex-direction: column;
}
#analyse {
  position: absolute;
  width: 90%;
  height: 30%;
  left: 5%;
  top: 25%;
  background: #c4c4c4;
  box-shadow: 6px 8px 8px #2e3244;
  display: flex;
  flex-direction: column;
}
#message {
  position: absolute;
  width: 90%;
  height: 25%;
  left: 5%;
  top: 60%;
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
}
</style>