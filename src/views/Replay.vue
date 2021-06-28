<template>
  <div class="replay">
    <div class="replay_audio">
      <div class="replay_audio_enregistrement">
        <audio controls id="audio"></audio>
      </div>
      <div class="replay_audio_button">
        <button class="replay_audio_button_enregistrer" id="enregistrer">
          Enregistrer
        </button>
        <button class="replay_audio_button_stop" id="arreter">Arrêter</button>
      </div>
    </div>
    <div class="replay_choix">
      <div class="replay_choix_button">
        <router-link to="/Test3_1">
          <button>
            <b>Accéder au diagnostique</b>
          </button>
        </router-link>
      </div>
    </div>
  </div>
</template>

<script>
// export default {
//   name: "Replay",

//   methods: {
//     enregistrer.onclick = () => {
//   navigator.mediaDevices.getUserMedia({ audio: true }).then((stream) => {
//     mediaRecorder = new MediaRecorder(stream);
//     mediaRecorder.start();
//     chuck = [];

//     mediaRecorder.addEventListener("dataavailable", (e) => {
//       blob = newBlob(e.data);
//     });
//     mediaRecorder.addEventListener("stop", (e) => {
//       blob = newBlob(chuck);
//       audio_url = URL.createObjectURL(blob);
//       audio = new Audio(audio_url);
//       audio.setAttribute("controls", 1);
//       ok.appendChild(audio);
//     });
//   });
// }
//   arreter.onclick = () => {
//   mediaRecorder.stop();
// }
// },
// }
</script>

<style scoped>
.replay {
  display: flex;
  justify-content: center;
  align-items: center;
  height: 80vh;
  width: 100vw;
  flex-direction: column;
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

button {
  box-shadow: 6px 8px 8px #2e3244;
  background: #f1895c;
  margin: 10px;
  height: 6vh;
  width: 50vw;
}
</style>