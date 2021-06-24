<template>
  <div class="Play">
    <div class="play_etape2">
      <p><b>Etape n°2</b></p>
    </div>
    <div class="gros_rectangle">
      <div class="rond_micro">
        <div class="micro">
          <router-link to="/Replay">
            <button>
              <img
                src="https://e7.pngegg.com/pngimages/135/8/png-clipart-microphone-computer-icons-microphone-electronics-microphone-thumbnail.png"
              />
            </button>
          </router-link>
        </div>
      </div>
    </div>
    <div class="texte_micro">
      <p><b>Maintenez le micro appuyé et toussez</b></p>
    </div>
  </div>
</template>

<script>
</script>


<style scoped>
#Play {
  display: flex;
  justify-content: center;
  align-items: center;
  height: 90vh;
  width: 100vw;
  flex-direction: column;
}

#play_etape2 {
  width: 25vw;
  height: 7vh;
  background: #f1895c;
  box-shadow: 6px 8px 8px #2e3244;
  font-weight: bold;
  display: flex;
  flex-direction: column;
  margin: 20px;
}

#micro {
  position: absolute;
  width: 135px;
  height: 132px;
  left: 668px;
  top: 363px;

  background: #516079;
}

#rond_micro  {
  position: absolute;
  width: 135px;
  height: 132px;
  left: 668px;
  top: 363px;

  background: #516079;
}

#texte_micro {
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

#gros_rectangle {
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