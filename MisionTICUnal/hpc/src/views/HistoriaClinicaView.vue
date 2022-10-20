<template>
    <div class="container">
    <table >
      <h1>Historia Clinica</h1>
      <!-- <tr>
        <th>Cedula</th>
        <th>Nombres</th>
        <th>Documento</th>
        <th>Apellidos</th>
        <th>Tel Contacto</th>
        <th>Email</th>
      </tr> -->
      <tr>

        <td>
          <input type="number" id="paciente_id" name="paciente_id" v-model="paciente_id" placeholder="PACIENTE ID">
        </td>
        <td>
          <input type="text" id="observaciones" name="observaciones" v-model="observaciones" placeholder="OBSERVACIONES">
        </td>
      </tr>
      <tr>
        <button v-on:click="registrar()">CREAR</button>
      </tr>
      <br><br><br>
      <tr>
        <th>ID</th>
        <th>ID Paciente</th>
        <th>Observaciones</th>
      </tr>
      <tr v-for="i in lista">
        <td>{{i.id}}</td>
        <td>{{i.paciente_id}}</td>
        <td>{{i.observaciones}}</td>
      <td>
        <button v-on:click="eliminar(i.id)">Eliminar</button>
      </td>
      <td>
        <button v-on:click="editar(i.id)">Editar</button>
      </td>
    </tr>
    </table>
  </div>
  </template>
  
  <script>
    import axios from 'axios';
  
    export default{
      name: "HistoriaClinicaView",
      data(){
        return {
          lista: null,
          paciente_id:"",
          observaciones:"",
      }
    },
  
    methods:{
      registrar(){
        let post = {
          "paciente_id": this.paciente_id,
          "observaciones": this.observaciones,
          
        }
  
        axios.post("http://127.0.0.1:8000/api/historia-clinica/", post)
        .then(result=>{
          this.paciente_id=""
          this.observaciones=""
          this.updated()
        })
  
      }
    },
  
      mounted(){
        let host = "http://127.0.0.1:8000/api/historia-clinica/";
        axios.get(host).then(data => {
          this.lista = data.data;
        })
      },
    
  
  }
  </script>
  