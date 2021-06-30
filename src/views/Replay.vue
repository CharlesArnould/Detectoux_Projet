<template>
  <button onclick="recordOnclick()" id='record'>Record</button>
  <button onclick="stopOnclick()" id='stop'>Stop</button>
  <div id="ok"></div>
</template>

<script>
/*
  recordOnclick = () =>{
    navigator.mediaDevices.getUserMedia({audio : true})
    .then(stream=>{

      mediaRecorder=new MediaRecorder(stream)
      mediaRecorder.start()
      chuck=[]

      mediaRecorder.addEventListener("dataavailable", e =>{
        chuck.push(e.data)
      })

      mediaRecorder.addEventListener("stop", e=>{
        blob=new Blob(chuck)
        audio_url=URL.createObjectURL(blob)
        audio=new Audio(audio_url)
        audio.setAttribute("controls",1)
        ok.appendChild(audio)
      })
      setTimeout(() => { mediaRecorder.stop();}, 5000);
    })
  }

  stopOnclick= () =>{
    mediaRecorder.stop()
  }
*/
</script>


<style scoped>
</style>

