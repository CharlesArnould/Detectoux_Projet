<template>
  <div class="play">
    <div class="play_etape2">
      <p><b>Etape 2</b></p>
    </div>

    <div class="play_rectangle">
      <div class="play_rectangle_rond">
        <div class="play_rectangle_rond_micro">
          <router-link to="/Replay">
            <button>
              <img
                src="https://e7.pngegg.com/pngimages/135/8/png-clipart-microphone-computer-icons-microphone-electronics-microphone-thumbnail.png"
              />
            </button>
          </router-link>
        </div>
      </div>
      <div class="play_rectangle_texte">
        <p><b>Maintenez le micro appuyé et toussez</b></p>
      </div>
    </div>
  </div>
</template>

<script>
</script>


<style scoped>
.play {
  display: flex;
  justify-content: center;
  align-items: center;
  height: 80vh;
  width: 100vw;
  flex-direction: column;
}

.play_etape2 {
  width: 25vw;
  height: 7vh;
  background: #f1895c;
  box-shadow: 6px 8px 8px #2e3244;
  font-weight: bold;
  display: flex;
  flex-direction: column;
  margin: 20px;
}

.play_rectangle {
  display: flex;
  justify-content: center;
  align-items: center;
  width: 90vw;
  height: 50vh;
  flex-direction: column;

  background: #c4c4c4;
}

.play_rectangle_rond {
  display: flex;
  justify-content: center;
  align-items: center;
  box-shadow: 6px 8px 8px #2e3244;
  width: 50vw;
  height: 30vh;

  background: #516079;
}

.play_rectangle_rond_micro {
  display: flex;
  justify-content: center;
  align-items: center;
  width: 20vw;
  height: 10vh;

  background: #516079;
}

.play_rectangle_texte {
  display: flex;
  justify-content: center;
  align-items: center;
  width: 70vw;
  height: 50vh;

  font-family: Raleway;
  font-style: normal;
  font-weight: normal;
  font-size: 14px;
  line-height: 16px;
  text-align: center;

  color: #2e3244;
}

button {
  width: 33px;
  height: 64px;
  left: 715px;
  top: 397px;
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