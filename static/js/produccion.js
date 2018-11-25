var app = new Vue({
  el: '#app',
  delimiters: ['[[',']]'],
  data: {
    germinaciones: [],
    cultivos: [],
    loading: true,
    showModal : false,
  },
  components: {
    'modal': httpVueLoader(BASE_URL+'/static/js/components/modal.vue')
  },
  mounted: function() {
    this.getAll();
  },
  methods: {
    getAll: function(){
      this.getGerminaciones();
      this.getCultivos();
    },
    getPlanta: function(id) {
      this.loading = true;
      this.$http.get(`/api/plantas/${id}/`)
          .then((response) => {
            this.currentPlanta = response.data;
          })
          .catch((err) => {
            this.loading = false;
            console.log(err);
          })
    },
    getCultivos: function() {
      let api_url = '/api/cultivos/';
      this.loading = true;
      this.$http.get(api_url)
          .then((response) => {
            this.cultivos = response.data;
            this.loading = false;

          })
          .catch((err) => {
            this.loading = false;
            console.log(err);
          })
    },
    getGerminaciones: function() {
      let api_url = '/api/germinaciones/';
      this.loading = true;
      this.$http.get(api_url)
          .then((response) => {
            this.germinaciones = response.data;
            this.loading = false;
          })
          .catch((err) => {
            this.loading = false;
            console.log(err);
          })
    },
    deleteCultivo: function(id) {
      this.loading = true;
      this.$http.delete(`/api/cultivos/${id}/`)
          .then((response) => {
            this.loading = false;
            this.getCultivos();
          })
          .catch((err) => {
            this.loading = false;
            console.log(err);
          })
    },
    deleteGerminacion: function(id) {
      this.loading = true;
      this.$http.delete(`/api/germinaciones/${id}/`)
          .then((response) => {
            this.loading = false;
            this.getGerminaciones();
          })
          .catch((err) => {
            this.loading = false;
            console.log(err);
          })
    },
    closeModal: function() {
      this.showModal = false;
    }
  }
});
    /*
    addPlanta: function() {
      this.loading = true;
      this.$http.post('/api/article/',this.newPlanta)
          .then((response) => {
            this.loading = true;
            this.getPlantas();
          })
          .catch((err) => {
            this.loading = true;
            console.log(err);
          })
    },
    */
