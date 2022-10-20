

<template>
  <div class="container">
  <table >
    <h1>Familiar</h1>
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
        <input type="number" id="tel_contacto" name="tel_contacto" v-model="tel_contacto" placeholder="TEL CONTACTO">
      </td>
      <td>
        <input type="text" id="email" name="email" v-model="email" placeholder="CORREO">
      </td>
    </tr>
    <tr>
      <button v-on:click="registrar()" class="">CREAR</button>
    </tr>
    <br><br><br>
    <tr style="coloar:red">
      <th>ID</th>
      <th>Cedula</th>
      <th>Nombres</th>
      <th>Apellidos</th>
      <th>Telefono</th>
      <th>Email</th>
    </tr>
    <tr v-for="i in lista">
      <td>{{i.id}}</td>
      <td>{{i.cedula}}</td>
      <td>{{i.nombres}}</td>
      <td>{{i.apellidos}}</td>
      <td>{{i.tel_contacto}}</td>
      <td>{{i.email}}</td>
    <td>
      <button v-on:click="eliminar(i.id)" class="btn btn-danger">Eliminar</button>
    </td>
    <td>
      <button v-on:click="editar(i.id)" class="btn btn-warning">Editar</button>
    </td>
  </tr>
  </table>
</div>
</template>


<script>
  import axios from 'axios';

  export default{
    name: "FamiliarView",
    data(){
      return {
        lista: null,
        id:"",
        cedula:"",
        nombres:"",
        apellidos:"",
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
        "tel_contacto": this.tel_contacto,
        "email": this.email,
      }

      axios.post("http://127.0.0.1:8000/api/familiar/", post)
      .then(result=>{
        this.id=""
        this.cedula=""
        this.nombres=""
        this.apellidos=""
        this.tel_contacto=""
        this.email=""
        this.updated()
      })

    }
  },

  editar(id){
    this.$router.push('edit/'+ id);
  },
  
  eliminar(id){
    console.log(id)
    axios.delete("http://127.0.0.1:8000/api/familiar/"+ id + "/").then(result=>{
        this.updated()

      })
  },

    mounted(){
      let host = "http://127.0.0.1:8000/api/familiar/";
      axios.get(host).then(data => {
        this.lista = data.data;
      })
    },
  

}


</script>
