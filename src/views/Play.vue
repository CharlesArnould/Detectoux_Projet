<template>
  <div id="rectangle">
    <p>Etape n°2</p>

    <div id="grandRectangle">
      <div class="home_choix_button">
        <router-link to="/Test1">
          <button>
            <b>Maintenez le bouton appuyé et toussez :')</b>
          </button>
        </router-link>
      </div>
    </div>
  </div>
</template>

<script>
</script>


<style scoped>
#rectangle {
  position: absolute;
  width: 300px;
  height: 264px;
  box-shadow: 0px 2px 3px #2e3244;
  background: #f1895c;
}

#grandRectangle {
  position: absolute;
  width: 1266px;
  height: 281px;
  left: 84px;
  top: 336px;

  background: #c4c4c4;
}

button {
  position: absolute;
  width: 33px;
  height: 64px;
  left: 715px;
  top: 397px;
}

p {
  position: absolute;
  width: 600px;
  height: 50px;
  left: 433px;
  top: 545px;

  font-family: Raleway;
  font-style: normal;
  font-weight: normal;
  font-size: 24px;
  line-height: 28px;
  text-align: center;
  color: #2e3244;
}
</style>