<template>
  <div class="test1">
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
            <select id="fum" required>
              <option value="">- Choix -</option>
              <option value="oui">Oui</option>
              <option value="non">Non</option>
            </select>
          </div>
          <br />
          <div class="test1_wrapper_rectangle_form_ant">
            <label for="sexe">Antécedents médicaux :&nbsp;</label>
            <select id="sexe" required>
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
            <label for="sexe">Symptômes :&nbsp;</label>
            <select id="sexe" required>
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
          <br />
          <div class="test1_wrapper_rectangle_form_audio">
            <section class="main-controls">
              <canvas class="visualizer" height="60px"></canvas>
              <div id="buttons">
                <button id="record" onclick="recordOnclick()">
                  Enregistrer
                </button>
              </div>
            </section>
            <section id="sound_clips"></section>
            <br />
          </div>
        </div>
      </div>
    </div>
    <div class="replay_choix">
      <div class="replay_choix_button">
        <router-link to="/Test3_1">
          <button>
            <b>Accéder au diagnostic</b>
          </button>
        </router-link>
      </div>
    </div>
  </div>
</template>

<script>
if (navigator.mediaDevices && navigator.mediaDevices.getUserMedia) {
  console.log("getUserMedia supported.");
  recordOnclick = function () {
    navigator.mediaDevices
      .getUserMedia({ audio: true })
      // Success callback
      .then((stream) => {
        mediaRecorder = new MediaRecorder(stream);
        mediaRecorder.start();
        console.log(mediaRecorder.state);
        console.log("recorder started");
        // record.style.background = "red";
        // record.style.color = "black";
        chuck = [];

        mediaRecorder.addEventListener("dataavailable", (e) => {
          chuck.push(e.data);
        });

        mediaRecorder.addEventListener("stop", (e) => {
          console.log("recorder stopped");
          const clipContainer = document.createElement("article");
          const clipLabel = document.createElement("p");
          const deleteButton = document.createElement("button");

          clipContainer.classList.add("clip");
          blob = new Blob(chuck, { type: "audio/ogg; codecs=opus" });
          audio_url = URL.createObjectURL(blob);
          audio = new Audio(audio_url);

          audio.setAttribute("controls", 1);
          deleteButton.innerHTML = "Delete";
          // clipLabel.innerHTML = "Votre toux";

          clipContainer.appendChild(audio);
          clipContainer.appendChild(clipLabel);
          clipContainer.appendChild(deleteButton);
          sound_clips.appendChild(clipContainer);

          deleteButton.onclick = function (e) {
            let evtTgt = e.target;
            evtTgt.parentNode.parentNode.removeChild(evtTgt.parentNode);
          };
        });
        setTimeout(() => {
          mediaRecorder.stop();
        }, 3000);
      })
      // Error callback
      .catch(function (err) {
        console.log("The following getUserMedia error occurred: " + err);
      });
  };
} else {
  console.log("getUserMedia not supported on your browser!");
}
</script>

<style scoped>
body {
  overflow: auto;
}

#record .test1 {
  display: flex;
  justify-content: center;
  align-items: center;
  height: 80vh;
  width: 100vw;
  flex-direction: column;
  margin: 0;
}

/* #record:active {
  background-color: red;
} */

.test1_wrapper {
  display: flex;
  justify-content: center;
  align-items: center;
  height: 50vh;
  width: 90vw;
  margin: 30px;
}

.test1_wrapper_rectangle {
  box-shadow: 6px 8px 8px #2e3244;
  background: #c4c4c4;
  display: flex;
  justify-content: center;
  align-items: center;
  padding: 40px;
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

/* .wrapper {
  display: flex;
  flex-direction: column;
} */

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

canvas {
  display: block;
  margin-bottom: 0.5rem;
}

/* #buttons {
  display: flex;
  flex-direction: row;
  justify-content: space-between;
} */

/* #buttons button {
  font-size: 1rem;
  padding: 1rem;
  width: calc(50% - 0.25rem);
} */
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

/* button:active {
  box-shadow: inset 0px 0px 20px rgba(0, 0, 0, 0.5);
  transform: translateY(2px);
} */

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

/* Checkbox hack to control information box display */

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
  .test1_wrapper_rectangle_form_audio {
    width: 90%;
    max-width: 1000px;
    margin: 0 auto;
  }
}
</style>