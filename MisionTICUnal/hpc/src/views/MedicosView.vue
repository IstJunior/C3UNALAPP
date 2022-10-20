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
          <input type="number" id="cedula" name="cedula" v-model="cedula" placeholder="CEDULA">
        </td>
        <td>
          <input type="text" id="nombres" name="nombres" v-model="nombres" placeholder="NOMBRES">
        </td>
        <td>
          <input type="text" id="apellidos" name="apellidos" v-model="apellidos" placeholder="APELLIDOS">
        </td>
        <td>
          <input type="text" id="especialidad" name="especialidad" v-model="especialidad" placeholder="ESPECIALIDAD">
        </td>
        <td>
          <input type="number" id="tel_contacto" name="tel_contacto" v-model="tel_contacto" placeholder="TEL CONTACTO">
        </td>
        <td>
          <input type="text" id="email" name="email" v-model="email" placeholder="CORREO">
        </td>
      </tr>
      <tr>
        <button v-on:click="registrar()">CREAR</button>
      </tr>
      <br><br><br>
      <tr>
        <th>ID</th>
        <th>Cedula</th>
        <th>Nombres</th>
        <th>Apellidos</th>
        <th>Especialidad</th>
        <th>Telefono</th>
        <th>Email</th>
      </tr>
      <tr v-for="i in lista">
        <td>{{i.id}}</td>
        <td>{{i.cedula}}</td>
        <td>{{i.nombres}}</td>
        <td>{{i.apellidos}}</td>
        <td>{{i.especialidad}}</td>
        <td>{{i.tel_contacto}}</td>
        <td>{{i.email}}</td>
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
      name: "MedicosView",
      data(){
        return {
          lista: null,
          id:"",
          cedula:"",
          nombres:"",
          apellidos:"",
          especialidad:"",
          tel_contacto:"",
          email:""
      }
    },
  
    methods:{
      registrar(){
        let post = {
          "cedula": this.cedula,
          "nombres": this.nombres,
          "apellidos": this.apellidos,
          "especialidad":this.especialidad,
          "tel_contacto": this.tel_contacto,
          "email": this.email,
        }
  
        axios.post("http://127.0.0.1:8000/api/medicos/", post)
        .then(result=>{
          this.cedula=""
          this.nombres=""
          this.apellidos=""
          this.especialidad=""
          this.tel_contacto=""
          this.email=""
          this.updated()
        })
  
      }
    },
  
      mounted(){
        let host = "http://127.0.0.1:8000/api/medicos/";
        axios.get(host).then(data => {
          this.lista = data.data;
        })
      },
    
  
  }
  </script>
  