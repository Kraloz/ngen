<template>
  <transition name="modal">
    <div class="modal-mask">
      <div class="modal-wrapper" @click="close()">
        <div class="modal-container" @click.stop>
          <button type="button" class="close" aria-label="Close" @click="close()"> <span aria-hidden="true">&times;</span></button>
          <div class="modal-header">
            
            <slot name="header">
              default header
            </slot>
          </div>

          <div class="modal-body">
            <div name="body">
              <form>
                <label for="nombre">Id</label>
                <input v-model="currentPlanta.id" type="text" name="id" id="id" readonly>
                <label for="nombre">Nombre</label>
                <input v-model="nombre" type="text" name="nombre" id="nombre">
                <label for="dias-germinacion">Germinacion</label>
                <input v-model="dias_germinacion" type="text" name="dias-germinacion" id="dias-germinacion">
                <label for="etapa-recoleccion">Recoleccion</label>
                <input v-model="etapa_recoleccion" type="text" name="etapa-recoleccion" id="etapa-recoleccion">
                <label for="riego">Riego</label>
                <input v-model="riego" type="text" name="riego" id="riego">
                <label for="maceta-litros">Maceta</label>
                <input v-model="maceta_litros" type="text" name="maceta-litros" id="maceta-litros">
                <label for="extra">Extra</label>
                <input v-model="extra" type="text" name="extra" id="extra">
              </form>
            </div>
          </div>
          <div class="modal-footer">
            <slot name="footer">
            </slot>
          </div>
        </div>
      </div>
    </div>
  </transition>
</template>


<script>
  module.exports = {
    name: 'modal',
    props:['currentPlanta'],
    data() {
      return {
        id: this.currentPlanta.id,
        nombre: this.currentPlanta.nombre,
        riego: this.currentPlanta.riego,
        dias_germinacion: this.currentPlanta.dias_germinacion,
        extra: this.currentPlanta.extra,
        etapa_recoleccion: this.currentPlanta.etapa_recoleccion,
        maceta_litros: this.currentPlanta.maceta_litros
      }
    },
    methods: {
      close() {
        app.closeModal();
      }
    }
  }
</script>


<style>
 .modal-mask {
  position: fixed;
  z-index: 9998;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background-color: rgba(0, 0, 0, .5);
  display: table;
  transition: opacity .3s ease;
}

.modal-wrapper {
  display: table-cell;
  vertical-align: middle;
}

.modal-container {
  width: 300px;
  margin: 0px auto;
  padding: 20px 30px;
  background-color: #fff;
  border-radius: 2px;
  box-shadow: 0 2px 8px rgba(0, 0, 0, .33);
  transition: all .3s ease;
  font-family: Helvetica, Arial, sans-serif;
}

.modal-header h3 {
  margin-top: 0;
  color: #42b983;
}

.modal-body {
  margin: 20px 0;
}

.modal-default-button {
  float: right;
}

/*
 * The following styles are auto-applied to elements with
 * transition="modal" when their visibility is toggled
 * by Vue.js.
 *
 * You can easily play with the modal transition by editing
 * these styles.
 */

.modal-enter {
  opacity: 0;
}

.modal-leave-active {
  opacity: 0;
}

.modal-enter .modal-container,
.modal-leave-active .modal-container {
  -webkit-transform: scale(1.1);
  transform: scale(1.1);
}
</style>