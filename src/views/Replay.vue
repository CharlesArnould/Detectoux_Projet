<template>
  <div class="replay">
    <div class="replay_étape2">
      <p><b>Etape 2</b></p>
    </div>
    <div class="replay_audio">
      <div class="replay_audio_record">
        <!-- <canvas class="visualizer" height="60px"></canvas> -->
        <div classe="replay_audio_record_button">
          <button id="record" onclick="recordOnclick()">Enregistrer</button>
        </div>

        <section id="sound_clips"></section>
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
        record.style.background = "red";
        record.style.color = "black";
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
          clipLabel.innerHTML = "Votre toux";

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
.replay {
  display: flex;
  justify-content: center;
  align-items: center;
  height: 80vh;
  width: 100vw;
  flex-direction: column;
}

.replay_étape2 {
  width: 25vw;
  height: 7vh;
  background: #f1895c;
  box-shadow: 6px 8px 8px #2e3244;
  font-weight: bold;
  display: flex;
  flex-direction: column;
  margin: 20px;
}

.replay_audio {
  padding: 50px;
}

/* .replay_audio_record{

} */

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
  font-family: "Lucida Sans", "Lucida Sans Regular", "Lucida Grande",
    "Lucida Sans Unicode", Geneva, Verdana, sans-serif;
  color: #2e3244;
}

button:hover,
button:focus {
  height: 6vh;
  width: 51vw;
}

/* Make the clips use as much space as possible, and
 * also show a scrollbar when there are too many clips to show
 * in the available space */
.sound-clips {
  flex: 1;
  overflow: auto;
}

section,
article {
  display: block;
}

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
  background: #4d8ae8;
  padding: 0.5rem 0.75rem;
  font-size: 0.8rem;
}

/* Checkbox hack to control information box display */

label {
  font-size: 3rem;
  position: absolute;
  top: 2px;
  right: 3px;
  z-index: 5;
  cursor: pointer;
  background-color: black;
  border-radius: 10px;
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

aside p {
  font-size: 1.2rem;
  margin: 0.5rem 0;
}

aside a {
  color: #666;
}

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