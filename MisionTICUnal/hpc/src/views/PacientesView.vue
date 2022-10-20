<template>
    <div class="container">
    <table >
      <h1>Pacientes</h1>
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
          <input type="number" id="id_paciente" name="id_paciente" v-model="id_paciente" placeholdeid="ID">
        </td>
         <td>
          <input type="number" id="id_familiar_designado" name="id_familiar_designado" v-model="id_familiar_designado" placeholder="Familiar designado">
        </td>
        <td>
          <input type="number" id="id_medico_designado" name="id_medico_designado" v-model="id_medico_designado" placeholder="Medico designado">
        </td>
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
          <input type="number" id="tel_contacto" name="tel_contacto" v-model="tel_contacto" placeholder="TEL CONTACTO">
        </td>
        <td>
          <input type="text" id="email" name="email" v-model="email" placeholder="CORREO">
        </td>
        <td>
          <input type="text" id="direccion" name="direccion" v-model="direccion" placeholder="DIRECCION">
        </td>
      </tr>
      <tr>
        <button v-on:click="registrar()">CREAR</button>
      </tr>
      <br><br><br>
      <tr>
        <th>ID</th>
        <th>ID Familiar</th>
        <th>ID Medico</th>
        <th>Cedula</th>
        <th>Nombres</th>
        <th>Apellidos</th>
        <th>Telefono</th>
        <th>Email</th>
        <th>Direccion</th>
      </tr>
      <tr v-for="i in lista">
        <td>{{i.id_paciente}}</td>
        <td>{{i.id_familiar_designado}}</td>
        <td>{{i.id_medico_designado}}</td>
        <td>{{i.cedula}}</td>
        <td>{{i.nombres}}</td>
        <td>{{i.apellidos}}</td>
        <td>{{i.tel_contacto}}</td>
        <td>{{i.email}}</td>
        <td>{{i.direccion}}</td>
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
      name: "PacientesView",
      data(){
        return {
          lista: null,
          id_paciente:"",
          id_familiar_designado:"",
          id_medico_designado:"",
          cedula:"",
          nombres:"",
          apellidos:"",
          tel_contacto:"",
          email:"",
          direccion:""
      }
    },
  
    methods:{
      registrar(){
        let post = {
          "id_paciente":this.id_paciente,
          "id_familiar_designado":this.id_familiar_designado,
          "id_medico_designado":this.id_medico_designado,
          "cedula": this.cedula,
          "nombres": this.nombres,
          "apellidos": this.apellidos,
          "tel_contacto": this.tel_contacto,
          "email": this.email,
          "direccion":this.direccion
        }
  
        axios.post("http://127.0.0.1:8000/api/pacientes/", post)
        .then(result=>{
          this.id_paciente=""
          this.id_familiar_designado=""
          this.id_medico_designado=""
          this.cedula=""
          this.nombres=""
          this.apellidos=""
          this.tel_contacto=""
          this.email=""
          this.direccion=""
          this.updated()
        })
  
      }
    },
  
      mounted(){
        let host = "http://127.0.0.1:8000/api/pacientes/";
        axios.get(host).then(data => {
          this.lista = data.data;
        })
      },
    
  
  }
  </script>
  