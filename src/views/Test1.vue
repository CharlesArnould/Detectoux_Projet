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
          <div class="test1_wrapper_rectangle_form_button">
            <router-link to="/Replay">
              <button>
                <b>Etape suivante</b>
              </button>
            </router-link>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
/* onSubmit () {
    axios.get('URL DE PHP MY ADMIN', {
      'fumeur': this.fumeur,
      'antecedents': this.antecedents,
      'symptomes': this.symptomes,
      
    }).then(response => {
      if (response.data.error) {
        console.log('error', response.data.error)
      } else {
        this.postStatus = true;

        console.log('success', response.data.message)
      }
    }).catch(error => {
      console.log(error.response)
    });
  }; */
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