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
          <div class="test1_wrapper_rectangle_form_fum">
            <label for="fum">Fumeur :&nbsp;</label>
            <select id="fum" v-model="smoker" required>
              <option value="">- Choix -</option>
              <option value="oui">Oui</option>
              <option value="non">Non</option>
            </select>
          </div>
          <br />
          <div class="test1_wrapper_rectangle_form_ant">
            <label for="med">Antécedents médicaux :&nbsp;</label>
            <select id="med" v-model="medhist" required>
              <option value="">- Choix -</option>
              <option value="diabete">Diabète avec complications</option>
              <option value="asthme">
                Asthme ou maladie pulmonaire chronique
              </option>
              <option value="ins-card">
                Insuffisance cardiaque congestive
              </option>
              <option value="aucun">Aucun</option>
            </select>
          </div>
          <br />
          <div class="test1_wrapper_rectangle_form_sympt">
            <label for="symp">Symptômes :&nbsp;</label>
            <select id="symp" v-model="symp" required>
              <option value="">- Choix -</option>
              <option value="toux">Toux nouvelle ou aggravée</option>
              <option value="mdg">Mal de gorge</option>
              <option value="ess">Essoufflement</option>
              <option value="ess_mdg_mdc">
                Essoufflement, mal de gorge, maux de corps
              </option>
              <option value="ess_toux">
                Essoufflement, Toux nouvelle ou aggravée
              </option>
              <option value="mdg_pdg_pdo">
                Mal de gorge, perte du goût, perte de l'odorat
              </option>
              <option value="fvr_fr_toux_mdg">
                Fièvre, frissons ou sueurs, toux nouvelle ou aggravée, mal de
                gorge
              </option>
              <option value="fvr_fr_ess_toux_mdg_pdg_pdo">
                Fièvre, frissons ou sueurs, essoufflement, toux nouvelle ou
                aggravée, mal de gorge, perte de goût, perte d'odorat
              </option>
              <option value="aucun">Aucun</option>
            </select>
          </div>
          <div class="test1_wrapper_rectangle_form_audio">
            <section class="main-controls">
              <canvas class="visualizer" height="60px"></canvas>

              <button id="record" onclick="recordOnclick()">Enregistrer</button>
            </section>

            <section id="sound_clips"></section>
            <div class="replay_choix">
              <div class="replay_choix_button">
                <router-link to="/Test3_1">
                  <button>
                    <b>Accéder au diagnostic</b>
                  </button>
                </router-link>
              </div>
            </div>
            <br />
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "Test1",
  components: {},
  data() {
    return {
      smoker: null,
      medhist: null,
      symp: null,
      blob: null,
    };
  },
  mounted() {
    console.log(navigator);
  },
  methods: {
    record() {
      if (navigator.mediaDevices && navigator.mediaDevices.getUserMedia) {
        navigator.mediaDevices
          .getUserMedia({
            audio: true,
          })
          // Success callback
          .then((stream) => {
            let mediaRecorder = new MediaRecorder(stream);
            mediaRecorder.start();
            console.log(mediaRecorder.state);
            console.log("recorder started");
            record.style.background = "red";
            record.style.color = "black";
            let chuck = [];

            mediaRecorder.addEventListener("dataavailable", (e) => {
              chuck.push(e.data);
            });

            mediaRecorder.addEventListener("stop", (e) => {
              console.log("recorder stopped");
              const clipContainer = document.createElement("article");
              const clipLabel = document.createElement("p");
              const deleteButton = document.createElement("button");

              clipContainer.classList.add("clip");
              this.blob = new Blob(chuck, {
                type: "audio/mp3;",
              });
              console.log(this.blob.type);
              let audio_url = URL.createObjectURL(this.blob);
              let audio = new Audio(audio_url);

              audio.setAttribute("controls", 1);
              deleteButton.innerHTML = "Delete";
              clipLabel.innerHTML = "Votre toux";

              clipContainer.appendChild(audio);
              clipContainer.appendChild(clipLabel);
              clipContainer.appendChild(deleteButton);
              sound_clips.appendChild(clipContainer);
              console.log(this.donnee);
              deleteButton.onclick = function (e) {
                let evtTgt = e.target;
                evtTgt.parentNode.parentNode.removeChild(evtTgt.parentNode);
              };
            });
            setTimeout(() => {
              mediaRecorder.stop();
            }, 2000);
          })
          // Error callback
          .catch(function (err) {
            console.log("The following getUserMedia error occurred: " + err);
          });
      }
    },
  },
  computed: {
    donnee: function () {
      return [this.smoker, this.medhist, this.symp, this.blob];
    },
  },
};
</script>

<style scoped>
.test1 {
  display: flex;
  justify-content: center;
  align-items: center;
  height: 80vh;
  width: 100vw;
  flex-direction: column;
  /* margin: 20px; */
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
  margin: 50px;
}

.test1_wrapper_rectangle {
  box-shadow: 6px 8px 8px #2e3244;
  background: #c4c4c4;
  display: flex;
  justify-content: center;
  align-items: center;
  padding: 50px;
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

.test1_wrapper_rectangle_form_fum {
  display: flex;
  justify-content: center;
  align-items: center;
}

.test1_wrapper_rectangle_form_ant {
  display: flex;
  justify-content: center;
  align-items: center;
  flex-direction: column;
}

.test1_wrapper_rectangle_form_sympt {
  display: flex;
  justify-content: center;
  align-items: center;
  flex-direction: column;
}

button {
  background: #f1895c;
  margin: 5px;
  height: 6vh;
  width: 50vw;
  font-family: "Lucida Sans", "Lucida Sans Regular", "Lucida Grande",
    "Lucida Sans Unicode", Geneva, Verdana, sans-serif;
  color: #2e3244;
  /* box-shadow: 6px 8px 8px #2e3244; */
}

button:hover,
button:focus {
  height: 6vh;
  width: 51vw;
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

html,
body {
  height: 100%;
}

body {
  font-family: "Helvetica Neue", Helvetica, Arial, sans-serif;
  font-size: 0.8rem;
}

.wrapper {
  height: 100%;
  display: flex;
  flex-direction: column;
}

h1,
h2 {
  font-size: 2rem;
  text-align: center;
  font-weight: normal;
  padding: 0.5rem 0 0 0;
}

.main-controls {
  padding: 0.5rem 0;
}

/*
button {
  font-size: 1rem;
  background: #0088cc;
  text-align: center;
  color: white;
  border: none;
  transition: all 0.2s;
  padding: 0.5rem;
}
*/
button:hover,
button:focus {
  height: 6vh;
  width: 51vw;
}

button:active {
  box-shadow: inset 0px 0px 20px rgba(0, 0, 0, 0.5);
  transform: translateY(2px);
}

/* Make the clips use as much space as possible, and
 * also show a scrollbar when there are too many clips to show
 * in the available space */
.sound-clips {
  flex: 1;
  overflow: auto;
}

/*
section, article {
  display: block;
}*/

.clip {
  padding-bottom: 1rem;
}

audio {
  width: 100%;
  display: block;
  margin: 1rem auto 0.5rem;
}

.clip p {
  display: inline-block;
  font-size: 1rem;
}

.clip button {
  font-size: 1rem;
  float: right;
}

button.delete {
  background: #f00;
  padding: 0.5rem 0.75rem;
  font-size: 0.8rem;
}

input[type="checkbox"] {
  position: absolute;
  top: -100px;
}

aside {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  transform: translateX(100%);
  transition: 0.3s all ease-out;
  background-color: #efefef;
  padding: 1rem;
}

/*
aside p {
  font-size: 1.2rem;
  margin: 0.5rem 0;
}

aside a {
  color: #666;
}
*/
/* Toggled State of information box */
input[type="checkbox"]:checked ~ aside {
  transform: translateX(0);
}

/* Cursor when clip name is clicked over */

.clip p {
  cursor: pointer;
}

/* Adjustments for wider screens */
@media all and (min-width: 800px) {
  /* Don't take all the space as readability is lost when line length
     goes past a certain size */
  .wrapper {
    width: 90%;
    max-width: 1000px;
    margin: 0 auto;
  }
}
</style>