<template>
    <div class="container">
    <table >
      <h1>Medicos</h1>
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
          <input type="number" id="paciente_id" name="paciente_id" v-model="paciente_id" placeholder="ID PACIENTE">
        </td>
        <td>
          <input type="text" id="oximetria" name="oximetria" v-model="oximetria" placeholder="OXIMETRIA">
        </td>
        <td>
          <input type="number" id="frecuencia_respiratoria" name="frecuencia_respiratoria" v-model="frecuencia_respiratoria" placeholder="FRECUENCIA R">
        </td>
        <td>
          <input type="text" id="frecuencia_cardiaca" name="frecuencia_cardiaca" v-model="frecuencia_cardiaca" placeholder="FRECUENCIA C">
        </td>
      </tr>
      <tr>
        <button v-on:click="registrar()">CREAR</button>
      </tr>
      <br><br><br>
      <tr>
        <th>ID</th>
        <th>ID Paciente</th>
        <th>Oximetria</th>
        <th>Frecuencia C</th>
        <th>Frecuencia R</th>
      </tr>
      <tr v-for="i in lista">
        <td>{{i.id}}</td>
        <td>{{i.paciente_id}}</td>
        <td>{{i.oximetria}}</td>
        <td>{{i.frecuencia_respiratoria}}</td>
        <td>{{i.frecuencia_cardiaca}}</td>
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
      name: "SignosVitalesView",
      data(){
        return {
          lista: null,
          id:"",
          paciente_id:"",
          oximetria:"",
          frecuencia_respiratoria:"",
          frecuencia_cardiaca:""
          
      }
    },
  
    methods:{
      registrar(){
        let post = {
          "id": this.id,
          "paciente_id": this.paciente_id,
          "oximetria": this.oximetria,
          "frecuencia_respiratoria":this.frecuencia_respiratoria,
          "frecuencia_cardiaca": this.frecuencia_cardiaca
        }
  
        axios.post("http://127.0.0.1:8000/api/signos-vitales/", post)
        .then(result=>{
          this.id=""
          this.paciente_id=""
          this.oximetria=""
          this.frecuencia_respiratoria=""
          this.frecuencia_cardiaca=""
          this.updated()
        })
  
      }
    },
  
      mounted(){
        let host = "http://127.0.0.1:8000/api/signos-vitales/";
        axios.get(host).then(data => {
          this.lista = data.data;
        })
      },
    
  
  }
  </script>
  